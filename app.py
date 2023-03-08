import streamlit as st

def app():
    # Set the app's title
    st.title("My Decision Helper")

    st.sidebar.header("Decisions")
    option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])


    # Add a chat input and buttons
    st.subheader("Buttons")
    button_grid = st.beta_container()
    with button_grid:
        col1, col2, col3 = st.beta_columns(3)
        if col1.button("I want to apprach the new lady"):
            chat_suggection = "I want to apprach the new lady"
        if col2.button("I want to start a new community"):
            chat_suggection = "I want to start a new community"
        if col3.chat_suggection("I want to learn swimming"):
            chat_input = "I want to learn swimming"

    # Display the chat input
    st.subheader("Output")
    st.write(chat_input)
    st.subheader("What is your decision in one sentence")
    chat_input = st.text_input("Enter your thought here:")

# Run the Streamlit app
if __name__ == "__main__":
    app()
