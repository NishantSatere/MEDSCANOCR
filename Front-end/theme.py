import streamlit as st

def set_theme(theme):
    if theme == "Light":
        st.markdown(
            """
            <style>
            body {
                color: black;
                background-color: white;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Dark":
        st.markdown(
            """
            <style>
            body {
                color: white;
                background-color: black;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

# Add a selectbox to the sidebar for theme selection
theme = st.sidebar.selectbox(
    "Select Theme",
    options=["Light", "Dark"],
    index=0
)

# Apply the selected theme
set_theme(theme)

# Your Streamlit app content goes here...
st.title("My Streamlit App")
st.write("Welcome to my Streamlit app!")
