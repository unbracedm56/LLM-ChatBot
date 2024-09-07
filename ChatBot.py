import os
from API_KEYS import groq_api_key
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import (BaseChatMessageHistory, InMemoryChatMessageHistory)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import streamlit as st

os.environ["GROQ_API_KEY"] = groq_api_key
model = ChatGroq(model="llama3-8b-8192")
store = {}
if "store" not in st.session_state:
    st.session_state.store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = InMemoryChatMessageHistory()
    return st.session_state.store[session_id]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer all questions to the best of your ability in {language}."),
        MessagesPlaceholder(variable_name="messages")
    ]
)
chain = prompt | model

config = {"configurable": {"session_id": 'storage'}}
message_history = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="messages")

st.title("ChatBot")

if "language" not in st.session_state:
    st.session_state.language = "english"

language_input = st.sidebar.chat_input("Change language")
if language_input:
    st.session_state.language = language_input

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    with st.chat_message("assistant"):
        st.write("Hi! How can I help you?")

history = get_session_history("storage")
for message in history.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    else:
        with st.chat_message("assistant"):
            st.write(message.content)


text = st.chat_input("Say something")
if text:
    with st.chat_message("user"):
        st.write(text)
    response = message_history.invoke({"messages": HumanMessage(content=text), "language": st.session_state.language}, config=config)
    with st.chat_message("assistant"):
        st.write(response.content)



