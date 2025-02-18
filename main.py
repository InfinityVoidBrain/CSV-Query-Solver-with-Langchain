import streamlit as st
from app.ui import display_ui

def main():
    st.set_page_config(page_title="CSV AI", layout="wide")
    display_ui()

if __name__ == "__main__":
    main()
