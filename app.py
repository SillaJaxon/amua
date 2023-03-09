import streamlit as st

def get_bot_response(user_input):
    # Here you can implement your chatbot logic to generate a response
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Define the layout of the app
st.set_page_config(page_title="Chatbot", page_icon=":speech_balloon:")

# Define the content of the app
st.title("Chatbot")

# Define the text input and send button
col1, col2 = st.beta_columns([4, 1])
with col1:
    user_input = st.text_input("You:", key="user_input")

if st.button("Send", key="send_button"):
    bot_response = get_bot_response(user_input)
    with col1:
        st.text_area("Bot:", value=bot_response, height=100, key="bot_response")
        st.session_state.bot_response_history.append(bot_response)
        st.session_state.user_input_history.append(user_input)

if "bot_response_history" not in st.session_state:
    st.session_state.bot_response_history = []
    st.session_state.user_input_history = []

if st.session_state.bot_response_history:
    st.write("Conversation History:")
    for i in range(len(st.session_state.bot_response_history)):
        st.write("You: " + st.session_state.user_input_history[i])
        st.write("Bot: " + st.session_state.bot_response_history[i])
