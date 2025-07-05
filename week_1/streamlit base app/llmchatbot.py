import streamlit as st
import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="AIzaSyCDyiafjDZo4pJf36HDz4QQtCgpCe2DD3E")

model = genai.GenerativeModel("gemini-1.5-flash")

def get_llm_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
st.title("🤖 Google Gemini Chatbot")

user_input = st.text_input("Ask something:")

if user_input:
    st.info("Generating response...")
    reply = get_llm_response(user_input)
    st.success(reply)
