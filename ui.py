import streamlit as st
from videoanalyser import build_agent

st.set_page_config(page_title="Youtube Video Analyser", layout="centered")
st.title("AI Youtube Video Analyser")

@st.cache_resource
def get_agent():
    return build_agent()

agent = get_agent()

#input box
video = st.text_input("Paste Youtube URL")
button = st.button("Analyse Video")

if video and button:
    with st.spinner("Analysing video..."):
        response = agent.run(
            f"Analyse this video: {video}"
        )
        st.markdown(response.content)
