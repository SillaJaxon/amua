import streamlit as st

def add_suggestion():
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
