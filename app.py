import streamlit as st
import sidebar
import suggestions
from streamlit_tags import st_tags

# Define the options for the buttons in the sidebar
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Define the layout of the app
st.set_page_config(page_title="My Decision Maker", page_icon=":dart:")

# Define the content of the main page
st.header("My Decision Maker")
st.subheader("Choose any option here to get you started ...")

# Define the sidebar
selected_option = sidebar.add_sidebar(options)

# Define the grid of buttons with generic suggestions
suggestions.add_suggestions()

# Define the text input and send button
col1, col2 = st.beta_columns([4, 1])
with col1:
    if "selected_suggestion" in st.session_state:
        text_input = st.text_input("Enter your decision here...", value=st.session_state.selected_suggestion)
    else:
        text_input = st.text_input("Enter your decision here...")
with col2:
    st.write("") # Add some space
    st.write("") # Add some space
    if st.button("", key="send_button", help="Send your decision"):
        if "selected_suggestion" in st.session_state:
            st.session_state.selected_suggestion = None
            text_input = ""
        else:
            st.session_state.text_input = text_input
            text_input = ""
    st.image("https://img.icons8.com/material-outlined/24/000000/send.png")
