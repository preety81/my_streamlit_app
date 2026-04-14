import streamlit as st 
from youtubeanalyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube video analyzer",
    layout="centered"
    
    
)
st.title("🤖AI YouTube Video Analyzer")
@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent = get_agent()

#input box
video_url = st.text_input("Enter YouTube Video Link")
button = st.button("Analyze video")

if video_url and button:
    with st.spinner("Analyzing video..."):
        response = agent.run(
            f"Analyze this video:{video_url}"
            
            
            
        )
    st.markdown("Analysis of report video")
    st.markdown(response.content)