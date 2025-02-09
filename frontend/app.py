import streamlit as st
import requests
import time

# Backend API URL (use 'backend' service name for Docker or localhost for local testing)
API_URL = "http://backend:8000/generate"
# API_URL = "http://127.0.0.1:8000/generate"

# Streamlit page configuration
st.set_page_config(page_title="LLM: Model Comparison with FastAPI", layout="wide")

# Page title
st.title("LLM: Model Comparison with FastAPI")
st.divider()

# Layout: Split into two sections - Prompt input and settings
col_prompt, col_settings = st.columns([2, 3])

# Prompt input section
with col_prompt:
    prompt = st.text_input(label="Ask me a question...")  # Input field for user prompt
    st.divider()
    submit_btn = st.button("Submit")  # Submit button to trigger API calls

# Model settings section (temperature & max tokens)
with col_settings:
    temperature = st.slider(label="Temperature", min_value=0.0, max_value=1.0, value=0.7)  # Temperature slider
    max_tokens = st.slider(label="Maximum Tokens", min_value=100, max_value=500, value=200, step=100)  # Max tokens slider

st.divider()

# Layout: Four columns for model responses
col_deepseek , col_gpt, col_gemini, col_claude, col_command = st.columns(5)

# DeepSeek Model
with col_deepseek:
    if submit_btn:
        with st.spinner("DeepSeek Thinking..."):  # Show loading spinner
            st.info("DeepSeek")  # Display model name
            start_time = time.perf_counter()  # Start timing request
            response = requests.get(
                f"{API_URL}/deepseek?prompt={prompt}&temperature={temperature}&max_tokens={max_tokens}"
            )
            if response.status_code == 200:
                st.success("DeepSeek Response")  # Success message
                st.write(response.json().get("response"))  # Display model response
            else:
                st.error("Error occurred while getting response.")  # Error handling
            end_time = time.perf_counter()  # End timing
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")  # Display response time

# OpenAI GPT Model
with col_gpt:
    if submit_btn:
        with st.spinner("GPT Thinking..."):  # Show loading spinner
            st.warning("OpenAI")  # Display model name
            start_time = time.perf_counter()  # Start timing request
            response = requests.get(
                f"{API_URL}/openai?prompt={prompt}&temperature={temperature}&max_tokens={max_tokens}"
            )
            if response.status_code == 200:
                st.success("GPT-4 Turbo Response")  # Success message
                st.write(response.json().get("response"))  # Display model response
            else:
                st.error("Error occurred while getting response.")  # Error handling
            end_time = time.perf_counter()  # End timing
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")  # Display response time

# Google Gemini Model
with col_gemini:
    if submit_btn:
        with st.spinner("Gemini Thinking..."):  # Show loading spinner
            st.info("Gemini Pro")  # Display model name
            start_time = time.perf_counter()  # Start timing request
            response = requests.get(
                f"{API_URL}/gemini?prompt={prompt}&temperature={temperature}"
            )
            if response.status_code == 200:
                st.success("Gemini Pro Response")  # Success message
                st.write(response.json().get("response"))  # Display model response
            else:
                st.error("Error occurred while getting response.")  # Error handling
            end_time = time.perf_counter()  # End timing
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")  # Display response time

# Anthropic Claude Model
with col_claude:
    if submit_btn:
        with st.spinner("Claude Thinking..."):  # Show loading spinner
            st.error("Claude")  # Display model name (red for differentiation)
            start_time = time.perf_counter()  # Start timing request
            response = requests.get(
                f"{API_URL}/anthropic?prompt={prompt}&temperature={temperature}&max_tokens={max_tokens}"
            )
            if response.status_code == 200:
                st.success("Claude 2.1 Response")  # Success message
                st.write(response.json().get("response"))  # Display model response
            else:
                st.error("Error occurred while getting response.")  # Error handling
            end_time = time.perf_counter()  # End timing
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")  # Display response time

# Cohere Command Model
with col_command:
    if submit_btn:
        with st.spinner("Command Thinking..."):  # Show loading spinner
            st.warning("Command")  # Display model name (yellow for differentiation)
            start_time = time.perf_counter()  # Start timing request
            response = requests.get(
                f"{API_URL}/command?prompt={prompt}&temperature={temperature}&max_tokens={max_tokens}"
            )
            if response.status_code == 200:
                st.success("Command Response")  # Success message
                st.write(response.json().get("response"))  # Display model response
            else:
                st.error("Error occurred while getting response.")  # Error handling
            end_time = time.perf_counter()  # End timing
            elapsed_time = end_time - start_time
            st.caption(f"| :hourglass: {round(elapsed_time)} seconds")  # Display response time
