import streamlit as st

def app():
    # Set the app's title
    st.title("My Decision Helper")

    st.sidebar.header("Decisions")
    option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

    # Create the main content area
    st.write(f"You selected {option}!")

    # Add a chat input and buttons
    st.subheader("Chat Input")
    chat_input = st.text_input("Enter your message:")
    st.subheader("Buttons")
    button_grid = st.beta_container()
    with button_grid:
        col1, col2, col3 = st.beta_columns(3)
        if col1.button("Button 1"):
            chat_input = "You clicked Button 1!"
        if col2.button("Button 2"):
            chat_input = "You clicked Button 2!"
        if col3.button("Button 3"):
            chat_input = "You clicked Button 3!"

    # Display the chat input
    st.subheader("Output")
    st.write(chat_input)

# Run the Streamlit app
if __name__ == "__main__":
    app()
