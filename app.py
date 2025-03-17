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

# Hardcoded login credentials (replace with env vars for better security)
VALID_USERNAME = os.getenv("BOT_USERNAME")
VALID_PASSWORD = os.getenv("BOT_PASSWORD")


# Initialize OpenAI client.
client = openai.AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION
)

# Function to get chatbot response
def chat(messages):
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=messages
    )
    return response.choices[0].message.content

# Initialize session state for login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login Form
if not st.session_state.authenticated:
    st.title("Login to Access Chatbot 🤖")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.authenticated = True
            st.success("Login successful! 🎉")
            st.rerun()
        else:
            st.error("Invalid username or password!")

# If authenticated, show chatbot
if st.session_state.authenticated:
    st.title("Azure OpenAI Chatbot 🤖")

    # Logout button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

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
        response = chat(st.session_state.messages)

        # Immediately display AI response
        with st.chat_message("assistant"):
            st.markdown(response)

        # Append AI message to history
        st.session_state.messages.append({"role": "assistant", "content": response})
