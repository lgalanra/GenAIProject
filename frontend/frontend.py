import streamlit as st
import requests

st.title("Gen AI RAG Application")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    response = requests.post("http://127.0.0.1:8000/ask/", json={"question": question})
    if response.status_code == 200:
        answer = response.json()["answer"]
        st.write(f"Answer: {answer}")
    else:
        st.write("Error: Could not find an answer")