import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyD0FMYaCDeJK6dJyLW8DukX9DvETkXsd3Y")

def query_gemini(prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-2.0-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Digiflex AI Chatbot")
user_input = st.text_input("Ask me anything about Digiflex!")
if st.button("Submit"):
    response = query_gemini(user_input)
    st.write(response)
