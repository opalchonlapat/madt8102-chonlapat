from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st
import os

# with st.sidebar:
#     gemini_api_key = st.text_input("Gemini API Key: ", 
#                                placeholder="Type your API Key here...", 
#                                type="password")
#     if "GOOGLE_API_KEY" not in os.environ:
#         os.environ["GOOGLE_API_KEY"] = gemini_api_key
#     llm = ChatGoogleGenerativeAI(
#             model="gemini-pro",
#             temperature=1
#         )

st.title("🤖 My chatbot app")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# user_input = st.chat_input()
# if user_input:
#     if not gemini_api_key:
#         st.info("Please add your Gemini API key to continue.")
#         st.stop()

#     st.session_state.messages.append({"role": "user", "content": user_input})
#     st.chat_message("user").write(user_input)
#     response = llm.invoke(st.session_state["messages"])
#     bot_response = response.content
#     st.session_state.messages.append({"role": "assistant", "content": bot_response})
#     st.chat_message("assistant").write(bot_response)