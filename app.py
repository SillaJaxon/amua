import streamlit as st
import sidebar
import suggestions

# Define the options for the buttons in the sidebar
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

# Define the layout of the app
st.set_page_config(page_title="My Decision Maker", page_icon=":dart:")

# Define the content of the main page
content = """
    <div style='display:flex;justify-content:center;'>
        <div style='width:75%;'>
            <h1 style='text-align:center;'>My Decision Maker</h1>
            <h2 style='text-align:center;'>Choose your fate...</h2>
            """ + sidebar.add_sidebar(options) + suggestions.add_suggestions() + """
            <br>
            <div style='text-align:center;'>
                """ + (st.text_input("Enter your decision here...", value=st.session_state.selected_suggestion) if "selected_suggestion" in st.session_state else st.text_input("Enter your decision here...")) + """
                <br>
                <br>
                <button style='margin:auto;display:block;' type="submit" class="btn btn-primary">Send</button>
            </div>
        </div>
    </div>
"""

st.markdown(content, unsafe_allow_html=True)
