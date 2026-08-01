
import streamlit as st
import openai
import anthropic
import requests
import os

st.title("🎬 YouTube SEO Transcriber")

url = st.text_input("YouTube URL")
prompt = st.text_area("Prompt", value="Summarize this transcript...")

if st.button("Process"):
    st.info("This would run your Whisper + Claude logic here.")
    # You would paste the functions from Step 2 here
