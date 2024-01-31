

# import streamlit as st
# import streamlit as st
# from PIL import Image
# from streamlit_option_menu import option_menu
# import io
# import time
# # Define hardcoded credentials (replace with a secure authentication system in a real app)
# correct_username = "user123"
# correct_password = "pass123"

# # Page configurations
# st.set_page_config(
#     page_title="Your Project Name",
#     page_icon=":rocket:",
#     layout="wide",
# )

# # Sidebar navigation
# selected = option_menu(
#     menu_title="Main Menu", 
#     options=["Home", "About", "Contact", "Login"],
#     icons=["house","book","envelope","house"],
#     menu_icon="cast",
#     orientation="horizontal",
#     default_index=0,
#     styles={
#         "icon":{"color":"red","font-size":"25px"},
#         "nav-link":{
#             "font-size":"25px",
#             "text-align":"left",
#             "--hover-color":"brown",
#             "margin":"0px",
#         },    
#     }
# )
 
# # Home page
# if selected == "Home":
#     st.write("This is the home page.")
# if "photo" not in st.session_state:
#     st.session_state["photo"] = "not done"

#     col1, col2, col3 = st.columns([1, 2, 1])

#     col1.markdown("# Welcome to my app:")
#     col1.markdown("Here is some info on the app:")

#     def change_photo_state():
#         st.session_state["photo"] = "done"
     
#     uploaded_file = col2.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf", "doc"], on_change=change_photo_state)
#     camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

#     if st.session_state["photo"] == "done": 
#         progress_bar = col2.progress(0)
#         for perc_completed in range(100):
#             time.sleep(0.04)
#             progress_bar.progress(perc_completed + 1)
#         col2.success("File uploaded successfully!")

#     col3.metric(label="Time", value="09:57", delta="3^")

#     with st.expander("Click to learn more"):
#         st.write("Photo uploaded", camera_photo)

#     if uploaded_file is not None:
#         file_extension = uploaded_file.name.split('.')[-1].lower()
#         if file_extension in ['jpg', 'jpeg', 'png']:
#             img = Image.open(io.BytesIO(uploaded_file.read()))
#             st.image(img)
#         elif file_extension == 'pdf':
#             st.success("PDF file uploaded. Displaying PDF is not supported yet.")
#             # Handle PDF file
#         elif file_extension == 'doc':
#             st.success("DOC file uploaded. Displaying DOC is not supported yet.")
#             # Handle DOC file

#     if camera_photo is not None:
#         st.image(camera_photo)

# # About page
# elif selected == "About":
#     st.write("e")
#     st.title("About Us")


# # Contact page
# elif selected == "Contact":
#     st.header(":mailbox: Get in Touch with us!")
#     contact_form = """
#         <form action="https://formsubmit.co/devangmestry3@gmail.com" method="POST">
#             <input type="hidden" name="_captcha" value="true">
#             <input type="text" name="name" placeholder="Your Name" required>
#             <input type="email" name="email"  placeholder="Your Email" required>  
#             <textarea name="message" placeholder="Your Message here"></textarea>
#             <button type="submit">Send</button>
#         </form>
#     """
#     st.markdown(contact_form, unsafe_allow_html=True)

#     # User local CSS file
#     with open("FormStyle.css", "r") as f:
#         css_content = f.read()
#     st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# # Login page
# elif selected == "Login":
#     # Login form
#     st.title("Login Page")
    
#     username=st.text_input("username")
#     password= st.text_input("Password:",type="password")
    
#     if st.button("Login"):
#         if username == correct_username and correct_password == correct_password:
#             st.success("Login Sussessful!")
#             st.write("# Main Content Area")
#             st.write("This is main content area of your project ")
#         else:
#             st.error("Invalid username or password. Please try with proper credaintials!")
            
    
# # Footer
# st.markdown("---")
# st.markdown("Your Project Name | © 2024")
# st.markdown("[GitHub Repository](https://github.com/your")


