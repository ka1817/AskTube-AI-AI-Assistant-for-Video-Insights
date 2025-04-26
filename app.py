import streamlit as st
import requests

st.set_page_config(page_title="🎬 AskTube AI", layout="centered", page_icon="🔍")
st.title("🔍 **AskTube AI**")
st.markdown("##### _Unlock Insights from Any YouTube Video Instantly_ 📽️💡")

if "video_entered" not in st.session_state:
    st.session_state.video_entered = False

with st.sidebar:
    st.header("🎥 Enter YouTube Video ID")
    st.markdown("Example: `dQw4w9WgXcQ`")
    video_id_input = st.text_input("🔗 Paste Video ID Below", placeholder="YouTube Video ID")
    if st.button("🚀 Submit"):
        if not video_id_input.strip():
            st.warning("⚠️ Please enter a valid YouTube video ID.")
        else:
            st.session_state.video_id = video_id_input.strip()
            st.session_state.video_entered = True
            st.success("✅ Video ID submitted!")

if st.session_state.video_entered:
    video_id = st.session_state.video_id
    st.subheader(f"🤔 Ask me anything about this video: `{video_id}`")
    st.video(f"https://www.youtube.com/watch?v={video_id}")

    st.markdown("💬 **Type your question below:**")
    question = st.text_area("✍️ Your Question", placeholder="What is this video about?", height=100)

    col1, col2 = st.columns([1, 5])
    with col1:
        ask_btn = st.button("🎤 Ask")

    with col2:
        if ask_btn:
            if not question.strip():
                st.warning("⚠️ Please enter a question.")
            else:
                with st.spinner("🤖 Thinking hard..."):
                    try:
                        response = requests.post(
                            "http://backend:4000/ask/",
                            params={"video_id": video_id, "question": question}
                        )
                        data = response.json()

                        if "answer" in data:
                            st.success("🧠 Answer:")
                            st.write(f"**{data['answer']}**")
                        else:
                            st.error(f"🚫 {data.get('error', 'Unknown error occurred.')}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"🌐 Connection error: `{e}`")

    st.markdown("---")
    st.caption("🔁 To analyze another video, enter a new Video ID in the sidebar.")

else:
    st.info("👈 Please enter a YouTube video ID in the sidebar to get started.")
