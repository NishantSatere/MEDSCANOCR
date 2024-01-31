import streamlit as st

# Define hardcoded credentials (replace with a secure authentication system in a real app)
correct_username = "user123"
correct_password = "pass123"

# Page configurations
st.set_page_config(
    page_title="Your Project Name",
    page_icon=":rocket:",
    layout="wide",
)

# Sidebar navigation
page = st.sidebar.selectbox("Select a page", ["Home", "About", "Contact", "Login"])

# Home page
if page == "Home":
    st.title("Welcome to Your Project!")
    st.write("This is the home page of your project. Customize it as needed.")

# About page
elif page == "About":
    st.title("About Your Project")
    st.write("Provide information about your project here.")

# Contact page
elif page == "Contact":
    

# Login page
elif page == "Login":
    # Login form
    st.title("Login Page")

    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login successful!")
            # Simulate redirect by updating the page variable
            st.write("# Main Content Area")
            st.write("This is the main content area of your project. Customize it as needed.")
        else:
            st.error("Invalid username or password. Please try again.")

# Footer
st.markdown("---")
st.markdown("Your Project Name | © 2024")
st.markdown("[GitHub Repository](https://github.com/yourusername/yourproject)")

with open("style.css", "r") as f:
    css_content = f.read()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)