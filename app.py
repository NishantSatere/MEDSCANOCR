import streamlit as st
from PIL import Image
import io
import time
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
title=st.sidebar.write("MEDSCANOCR")
page = st.sidebar.selectbox("Select a page", ["Home", "About", "Contact", "Login"])

# Home page
if page == "Home":
    st.write("This is the home page.")




if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

col1, col2, col3 = st.columns([1, 2, 1])

col1.markdown("# Welcome to my app:")
col1.markdown("Here is some info on the app:")

def change_photo_state():
    st.session_state["photo"] = "done"
 
uploaded_file = col2.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf", "doc"], on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done": 
    progress_bar = col2.progress(0)
    for perc_completed in range(100):
        time.sleep(0.04)
        progress_bar.progress(perc_completed + 1)
    col2.success("File uploaded successfully!")

col3.metric(label="Time", value="09:57", delta="3^")

with st.expander("Click to learn more"):
    st.write("Photo uplodaed",camera_photo)

if uploaded_file is not None:
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension in ['jpg', 'jpeg', 'png']:
        img = Image.open(io.BytesIO(uploaded_file.read()))
        st.image(img)
    elif file_extension == 'pdf':
        st.success("PDF file uploaded. Displaying PDF is not supported yet.")
        # Handle PDF file
    elif file_extension == 'doc':
        st.success("DOC file uploaded. Displaying DOC is not supported yet.")
        # Handle DOC file

if camera_photo is not None:
    st.image(camera_photo)


    
# About page
elif page == "About":
    st.title("About Your Project")
    st.write("Provide information about your project here.")

# Contact page
elif page == "Contact":
    st.title("Contact Us")
    st.write("Contact information goes here.")

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


