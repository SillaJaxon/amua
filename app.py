import streamlit as st

# Define the options for the buttons in the sidebar
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Define the layout of the app
st.set_page_config(page_title="My Decision Maker", page_icon=":dart:")

# Define the sidebar
st.sidebar.title("Options")
selected_option = st.sidebar.radio("", options)

# Define the content of the main page
st.header("My Decision Maker")
st.subheader("Choose your fate...")

# Define the grid of buttons with generic suggestions
col1, col2, col3 = st.beta_columns(3)
with col1:
    if st.button("Do it"):
        st.session_state.selected_suggestion = "Do it"
with col2:
    if st.button("Don't do it"):
        st.session_state.selected_suggestion = "Don't do it"
with col3:
    if st.button("Ask someone else"):
        st.session_state.selected_suggestion = "Ask someone else"

col4, col5, col6 = st.beta_columns(3)
with col4:
    if st.button("Yes"):
        st.session_state.selected_suggestion = "Yes"
with col5:
    if st.button("No"):
        st.session_state.selected_suggestion = "No"
with col6:
    if st.button("Maybe"):
        st.session_state.selected_suggestion = "Maybe"

col7, col8, col9 = st.beta_columns(3)
with col7:
    if st.button("Try again"):
        st.session_state.selected_suggestion = "Try again"
with col8:
    if st.button("Wait"):
        st.session_state.selected_suggestion = "Wait"
with col9:
    if st.button("Think about it more"):
        st.session_state.selected_suggestion = "Think about it more"

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
