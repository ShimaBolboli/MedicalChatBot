import streamlit as st
import ollama

# Define the model creation script for medical advice
modelfile = '''
FROM llama3
SYSTEM You are an expert in the field of medical advice
'''

# Create the model (assuming the 'ollama.create' function works synchronously)
ollama.create(model='medical_advice_chat_bot', modelfile=modelfile)

# Title of the app
st.title("Medical Advice Chatbot")

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Input for user query
query = st.text_input("Ask your medical-related question:")

# Display response if query is entered
if query:
    response = ollama.chat(model='medical_advice_chat_bot', messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])
    # Update conversation history
    st.session_state.history.append({'role': 'user', 'content': query})
    st.session_state.history.append({'role': 'bot', 'content': response['message']['content']})

# Display the conversation history
for message in st.session_state.history:
    if message['role'] == 'user':
        st.markdown(f"*You:* {message['content']}")
    else:
        st.markdown(f"*Bot:* {message['content']}")
