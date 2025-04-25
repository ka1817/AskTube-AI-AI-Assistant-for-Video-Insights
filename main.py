from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os

import asyncio
from concurrent.futures import ThreadPoolExecutor

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = FastAPI(title="YouTube Transcript Q&A with LangChain (Async)")

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="""
You are a helpful assistant. Answer only from the provided transcript content. If the content is insufficient, just say you don't know.

{context}
Question: {question}
""",
    input_variables=["context", "question"]
)

def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

executor = ThreadPoolExecutor()

async def get_transcript_async(video_id: str):
    try:
        loop = asyncio.get_event_loop()
        transcript_list = await loop.run_in_executor(executor, YouTubeTranscriptApi.get_transcript, video_id, ["en"])
        return " ".join(chunk["text"] for chunk in transcript_list)
    except TranscriptsDisabled:
        return {"error": "Transcript not available for this video."}
    except Exception as e:
        return {"error": str(e)}

@app.post("/ask/")
async def ask_question(
    video_id: str = Query(..., description="YouTube video ID"),
    question: str = Query(..., description="Question based on video transcript")
):
    transcript_result = await get_transcript_async(video_id)
    if isinstance(transcript_result, dict) and "error" in transcript_result:
        return transcript_result

    transcript = transcript_result

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.create_documents([transcript])

    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })
    parser = StrOutputParser()
    main_chain = parallel_chain | prompt | llm | parser

    try:
        result = await asyncio.to_thread(main_chain.invoke, question)
        return {"answer": result}
    except Exception as e:
        return {"error": f"Failed to generate answer: {str(e)}"}


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port=4000)