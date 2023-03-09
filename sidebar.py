import streamlit as st

def add_sidebar(options):
    st.sidebar.title("Options")
    selected_option = st.sidebar.radio("", options)
    return selected_option
