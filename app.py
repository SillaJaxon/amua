import streamlit as st
from transformers import pipeline

# Define a function to generate a response from GPT-2 model
def generate_response(prompt):
    # Load the GPT-2 model
    generator = pipeline('text-generation', model='gpt2')

    # Generate a response to the prompt
    response = generator(prompt, max_length=1000, num_return_sequences=1)[0]['generated_text']

    return response

# Define the Streamlit app
def app():
    # Set the app's title
    st.title("Chat with ChatGPT")

    # Create a sidebar menu
    st.sidebar.header("Settings")
    prompt = st.sidebar.text_input("Prompt", "Hello, how are you?")
    submit_button = st.sidebar.button("Submit")

    # Create a chat window
    st.markdown("---")
    st.markdown("### Chat")

    chat_history = []
    if submit_button:
        # Add the user's prompt to the chat history
        chat_history.append(("User", prompt))

        # Generate a response to the user's prompt
        response = generate_response(prompt)

        # Add the response to the chat history
        chat_history.append(("ChatGPT", response))

    # Display the chat history
    for speaker, text in chat_history:
        if speaker == "User":
            st.write(f"You: {text}")
        else:
            st.write(f"ChatGPT: {text}")

# Run the Streamlit app
if __name__ == "__main__":
    app()
