import streamlit as st
import sidebar
import grid

# Define the options for the buttons in the sidebar
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Define the layout of the app
st.set_page_config(page_title="My Decision Maker", page_icon=":dart:")

# Define the content of the main page
st.header("My Decision Maker")
st.subheader("Choose your fate...")

# Define the sidebar
selected_option = sidebar.add_sidebar(options)

# Define the grid of buttons with generic suggestions
grid.add_grid()

# Define the text input and send button
if "selected_suggestion" in st.session_state:
    st.text_input("Enter your decision here...", value=st.session_state.selected_suggestion)
else:
    text_input = st.text_input("Enter your decision here...")

if st.button("Send"):
    if "selected_suggestion" in st.session_state:
        st.session_state.selected_suggestion = None
        text_input = ""
    else:
        st.session_state.text_input = text_input
        text_input = ""
