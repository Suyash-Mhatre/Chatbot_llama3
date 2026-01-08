from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

st.title("LANGCHAIN Demo with OLLAMA")
input_text = st.text_input("Search the topic you want")

llm = Ollama(model="llama3")
parser = StrOutputParser()

chain = prompt | llm | parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
