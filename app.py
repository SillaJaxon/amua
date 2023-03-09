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

# Define the grid of buttons
col1, col2, col3 = st.beta_columns(3)
with col1:
    st.button("Button 1")
with col2:
    st.button("Button 2")
with col3:
    st.button("Button 3")

col4, col5, col6 = st.beta_columns(3)
with col4:
    st.button("Button 4")
with col5:
    st.button("Button 5")
with col6:
    st.button("Button 6")

col7, col8, col9 = st.beta_columns(3)
with col7:
    st.button("Button 7")
with col8:
    st.button("Button 8")
with col9:
    st.button("Button 9")

# Define the text input at the bottom of the page
st.text_input("Enter your decision here...")
