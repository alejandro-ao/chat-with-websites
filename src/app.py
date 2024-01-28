# pip install streamlit langchain lanchain-openai

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "I don't know"

# app config
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")
if "chat_history" not in st.session_state:
  st.session_state.chat_history = [
    AIMessage(content="Hello, I am a bot. How can I help you?"),
  ]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")
    
# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
  response = get_response(user_query)
  st.session_state.chat_history.append(HumanMessage(content=user_query))
  st.session_state.chat_history.append(AIMessage(content=response))
  
# conversation 
for message in st.session_state.chat_history:
  if isinstance(message, AIMessage):
    with st.chat_message("AI"):
      st.write(message.content)
  elif isinstance(message, HumanMessage):
    with st.chat_message("Human"):
      st.write(message.content)
      