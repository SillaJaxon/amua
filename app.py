import streamlit as st

# Define the Streamlit app
def app():
    # Set the app's title
    st.title("My Streamlit App")

    # Create a sidebar menu
    st.sidebar.header("Settings")
    option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

    # Create the main content area
    st.write(f"You selected {option}!")

# Run the Streamlit app
if __name__ == "__main__":
    app()
