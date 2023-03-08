import streamlit as st

st.set_page_config(page_title="Decision Maker App", page_icon=":thinking_face:")

st.title("Decision Maker App")

# initialize variables
if "options" not in st.session_state:
    st.session_state.options = ["" for i in range(2)]

if "step" not in st.session_state:
    st.session_state.step = 1

if "reasons" not in st.session_state:
    st.session_state.reasons = {opt: [] for opt in st.session_state.options}

if "votes" not in st.session_state:
    st.session_state.votes = {opt: 0 for opt in st.session_state.options}

# define chatbot message and input functions
def chatbot_message(msg):
    st.write("Bot: " + msg)

def chatbot_input(label, key):
    return st.text_input("You: " + label, key=key)

# define function to handle option inputs
def handle_option_input(i):
    if i < len(st.session_state.options) - 1:
        chatbot_message("Please enter your next option:")
    else:
        chatbot_message("Thank you for entering your options.")
        st.session_state.step += 1

# define function to handle reason inputs
def handle_reason_input(option):
    if option in st.session_state.reasons and st.session_state.reasons[option]:
        chatbot_message(f"Please enter your next reason for {option}:")
    else:
        chatbot_message(f"Please enter a reason for {option}:")
    st.session_state.step += 1

# define function to handle vote inputs
def handle_vote_input():
    chatbot_message("Please vote on the following options:")
    for option, reasons in st.session_state.reasons.items():
        st.write(f"{option}: {len(reasons)} reasons")
        st.session_state.votes[option] = st.number_input(f"Vote for {option}", value=0, step=1, key=option)
    st.session_state.step += 1

# handle chat input based on current step
if st.session_state.step == 1:
    chatbot_message("Please enter the problem you need to make a decision about:")
    st.session_state.step += 1
elif st.session_state.step == 2:
    option_input = chatbot_input("Please enter your first option:", "option_input")
    if option_input:
        st.session_state.options.append(option_input)
        handle_option_input(len(st.session_state.options) - 1)
elif st.session_state.step == 3:
    for i, option in enumerate(st.session_state.options):
        if not st.session_state.reasons[option]:
            reason_input = chatbot_input(f"Please enter a reason for {option}:", f"reason_input_{option}")
        else:
            reason_input = chatbot_input(f"Please enter your next reason for {option}:", f"reason_input_{option}")
        if reason_input:
            st.session_state.reasons[option].append(reason_input)
            handle_reason_input(option)
            break
    else:
        handle_vote_input()
elif st.session_state.step == 4:
    chatbot_message("Thank you for voting! Here are the results:")
    for option, reasons in st.session_state.reasons.items():
        st.write(f"{option}: {len(reasons)} reasons, {st.session_state.votes[option]} votes")
    st.session_state.step += 1

# create restart button
if st.session_state.step > 4:
    if st.button
