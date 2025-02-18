import streamlit as st
from app.logic import get_data


def display_ui():
    st.title("Streamlit on Google Colab")
    st.write("This app is running on Google Colab using ngrok.")

    data = get_data()
    st.write("Sample Data:", data)
