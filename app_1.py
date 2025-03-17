import streamlit as st
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Access API keys and settings
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# Initialize OpenAI client
client = openai.AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION
)

# Chatbot UI
st.title("Azure OpenAI Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Immediately display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=st.session_state.messages
    ).choices[0].message.content

    # Immediately display AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Append AI message to history
    st.session_state.messages.append({"role": "assistant", "content": response})
