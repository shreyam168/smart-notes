import streamlit as st
from utils import summarize_text

st.title("Smart Notes App")

text = st.text_area("Enter your text")

if st.button("Summarize"):
    summary = summarize_text(text)
    st.write(summary)