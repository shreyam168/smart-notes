import streamlit as st

st.title("Smart Notes App")

text = st.text_area("Enter your text")

if st.button("Summarize"):
    st.write("Summary will appear here")