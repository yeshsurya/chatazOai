import streamlit as st

client = AzureOpenAI(
  api_key=api_key,  
  azure_endpoint=azure_endpoint,
  api_version=api_version
)

prompt = st.chat_input("First Part")
prompt2 = st.chat_input("Second Part")
if prompt:
    st.write(f"User has sent the following prompt: {prompt} --- {prompt2}")