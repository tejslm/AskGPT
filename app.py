from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GEMINI_API_KEY = os.getenv("gemini_api_key")

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                           google_api_key=GEMINI_API_KEY)

st.title("TejGPT")
question = st.text_input("Ask your question")

if st.button("Submit"):
    if question:
        answer=llm.invoke(question)
        st.write(answer.content)
    else:
        print("Please enter a question")

