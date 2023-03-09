import streamlit as st

def add_suggestions():
    suggestion1 = "Tell the HR about your toxic work environment"
    suggestion2 = "Start morning runs three times a week"
    suggestion3 = "Start learning web3 Technology"
    suggestion4 = "Pitch your new idea to your friend of buying land in Kamulu"
    suggestion5 = "Stop talking to your now toxic girlfriend for a while"
    suggestion6 = "Apply for a car loan at your chama"
    suggestion7 = "Plan on shifting to a bigger house"
    suggestion8 = "Optimize your code of the Streamlit app"
    suggestion9 = "Avoid using Ngong Road during rush hour"

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        if st.button(suggestion1, key="suggestion1"):
            st.session_state.selected_suggestion = suggestion1
    with col2:
        if st.button(suggestion2, key="suggestion2"):
            st.session_state.selected_suggestion = suggestion2
    with col3:
        if st.button(suggestion3, key="suggestion3"):
            st.session_state.selected_suggestion = suggestion3

    col4, col5, col6 = st.beta_columns(3)
    with col4:
        if st.button(suggestion4, key="suggestion4"):
            st.session_state.selected_suggestion = suggestion4
    with col5:
        if st.button(suggestion5, key="suggestion5"):
            st.session_state.selected_suggestion = suggestion5
    with col6:
        if st.button(suggestion6, key="suggestion6"):
            st.session_state.selected_suggestion = suggestion6

    col7, col8, col9 = st.beta_columns(3)
    with col7:
        if st.button(suggestion7, key="suggestion7"):
            st.session_state.selected_suggestion = suggestion7
    with col8:
        if st.button(suggestion8, key="suggestion8"):
            st.session_state.selected_suggestion = suggestion8
    with col9:
        if st.button(suggestion9, key="suggestion9"):
            st.session_state.selected_suggestion = suggestion9

    # Set the width of the buttons to be the same
    st.markdown("""<style>.streamlit-button{width:100%}</style>""", unsafe_allow_html=True)
