import streamlit as st
import requests

st.set_page_config(page_title="AskTube AI", layout="centered")
st.title("🔎 AskTube AI: Unlock Video Insights Instantly")

if "video_entered" not in st.session_state:
    st.session_state.video_entered = False

with st.sidebar:
    st.header("📺 Enter Video ID")
    video_id_input = st.text_input("YouTube Video ID", help="Example: dQw4w9WgXcQ")
    if st.button("Enter"):
        if not video_id_input.strip():
            st.warning("Please enter a valid YouTube video ID.")
        else:
            st.session_state.video_id = video_id_input.strip()
            st.session_state.video_entered = True

if st.session_state.video_entered:
    video_id = st.session_state.video_id
    st.subheader(f"Ask a question about 📹 `{video_id}`")
    question = st.text_area("Your Question", height=100)

    if st.button("Ask"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("🤖 Thinking..."):
                try:
                    response = requests.post(
                        "http://backend:4000/ask/",
                        params={"video_id": video_id, "question": question}
                    )
                    data = response.json()

                    if "answer" in data:
                        st.success("✅ Answer:")
                        st.write(data["answer"])
                    else:
                        st.error(data.get("error", "Unknown error occurred."))

                except requests.exceptions.RequestException as e:
                    st.error(f"Connection error: {e}")
else:
    st.info("Please enter a YouTube video ID in the sidebar to begin.")
