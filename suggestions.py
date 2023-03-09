import streamlit as st

def add_suggestions():
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        if st.button("Do it", key="do_it"):
            st.session_state.selected_suggestion = "Wake up early for a morning run 3 times a week"
    with col2:
        if st.button("Don't do it", key="dont_do_it"):
            st.session_state.selected_suggestion = "Don't do it"
    with col3:
        if st.button("Ask someone else", key="ask_someone_else"):
            st.session_state.selected_suggestion = "Ask someone else"

    col4, col5, col6 = st.beta_columns(3)
    with col4:
        if st.button("Yes", key="yes"):
            st.session_state.selected_suggestion = "Yes"
    with col5:
        if st.button("No", key="no"):
            st.session_state.selected_suggestion = "No"
    with col6:
        if st.button("Maybe", key="maybe"):
            st.session_state.selected_suggestion = "Maybe"

    col7, col8, col9 = st.beta_columns(3)
    with col7:
        if st.button("Try again", key="try_again"):
            st.session_state.selected_suggestion = "Try again"
    with col8:
        if st.button("Wait", key="wait"):
            st.session_state.selected_suggestion = "Wait"
    with col9:
        if st.button("Think about it more", key="think_about_it_more"):
            st.session_state.selected_suggestion = "Think about it more"
            
    # Set the width of the buttons to be the same
    st.markdown("""<style>.streamlit-button{width:100%}</style>""", unsafe_allow_html=True)
