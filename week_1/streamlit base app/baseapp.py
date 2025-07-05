import streamlit as st

# Mock function to simulate LLM response
def get_mock_response(prompt):
    return f"You asked: '{prompt}' — Here's a mock reply from the AI."

st.title("Simple LLM Chat App")

user_input = st.text_input("Enter your question:")

if user_input:
    response = get_mock_response(user_input)
    st.success(response)
