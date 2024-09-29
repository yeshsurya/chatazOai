import streamlit as st
from openai import AzureOpenAI

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=" ",
    azure_endpoint=" ",
    api_version="2024-07-01-preview"
)



# Function to get a response from the Azure OpenAI model
def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"You are an helpful AI bot"},
        {"role":"user","content":prompt}]
    )
    return response.choices[0].message.content

# Streamlit app layout
st.title("Azure OpenAI Chatbot")
user_input = st.text_input("You: ", "")
if st.button("Send"):
    if user_input:
        response = get_response(user_input)
        st.text_area("Bot:", value=response, height=200, max_chars=None, key=None)
    else:
        st.warning("Please enter a message.")