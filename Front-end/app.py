import streamlit as st
from openai import OpenAI
import pickle
from my_functions import increase_font_size, extract_test_results
import pytesseract
import cv2
import json
from pymongo import MongoClient
import time
import io
from PIL import Image


from streamlit_option_menu import option_menu
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define hardcoded credentials (replace with a secure authentication system in a real app)
correct_username = "user123"
correct_password = "pass123"

# Initialize session state
if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

# Page configurations lists
st.set_page_config(
    page_title="Your Project Name",
    page_icon=":bot:",
    layout="wide",
)

# Sidebar navigation menu
selected = option_menu(
    menu_title="MEDSCANOCR", 
    options=["Home", "About", "Contact", "Login", "Med-Bot"],
    icons=["house", "book", "envelope", "house", "bot"],
    menu_icon="cast",
    orientation="horizontal",
    default_index=0,
    styles={
        "icon":{"color":"red","font-size":"25px"},
        "nav-link":{
            "font-size":"25px",
            "text-align":"left",
            "--hover-color":"brown",
            "margin":"0px",
        },    
    }
)

# Home page
if selected == "Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    col1.markdown("# Welcome to my app: MEDSCANOCR ")
    def change_photo_state():
        st.session_state["photo"] = "done"
     
    # uploaded_file = col2.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf", "doc"], on_change=change_photo_state)
    camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

    if st.session_state["photo"] == "done": 
        progress_bar = col2.progress(0)
        for perc_completed in range(100):
            time.sleep(0.04)
            progress_bar.progress(perc_completed + 1)
        col2.success("File uploaded successfully!")

    col3.metric(label="Time", value="09:57", delta="3^")

    with st.expander("Click to learn more"):
        st.write("Photo uploaded", camera_photo)

    # if uploaded_file is not None:
    #     file_extension = uploaded_file.name.split('.')[-1].lower()
    #     if file_extension in ['jpg', 'jpeg', 'png']:
    #         img = Image.open(io.BytesIO(uploaded_file.read()))
    #         st.image(img)
    #     elif file_extension == 'pdf':
    #         st.success("PDF file uploaded. Displaying PDF is not supported yet.")
    #     elif file_extension == 'doc':
    #         st.success("DOC file uploaded. Displaying DOC is not supported yet.")

    # if camera_photo is not None:
    #     st.image(camera_photo)

    # Image Processing and Text Extraction
    uploaded_file_img_proc = st.file_uploader("Choose an image...", type=["jpg", "png", "pdf"])

    if uploaded_file_img_proc is not None:
        # Read the content of the uploaded file
        image_content = uploaded_file_img_proc.read()

        # Example usage
        image_path = 'uploaded_image.png'
        output_path = 'output_image.jpg'
        font_size_multiplier = 2.0

        # Save the uploaded file content to 'uploaded_image.png'
        with open(image_path, 'wb') as image_file:
            image_file.write(image_content)

        # Perform image processing and text extraction
        increase_font_size(image_path, output_path, font_size_multiplier)
        img = cv2.imread(output_path)
        text = pytesseract.image_to_string(img)

        # Display the processed image
        # st.image(img, caption='Processed Image', use_column_width=True)

        # Display the extracted text
        # st.subheader("Extracted Text:")
        # st.text(text)

        # Extract information and convert to JSON
        patient_info = extract_test_results(text)
        json_data = json.dumps(patient_info, indent=2)
        json_dict = json.loads(json_data)

        # Display the JSON data
        # st.subheader("Extracted Information (JSON):")
        # st.json(patient_info)

        # Save the JSON data to MongoDB
        mongo_client = MongoClient("mongodb+srv://nishant-satere:nishant-satere-2810@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority")
        db = mongo_client["patient"]
        collection = db["patient"]

        # Insert data into MongoDB
        result = collection.insert_one(json_dict)
        st.success(f"Data saved to MongoDB with ObjectID: {result.inserted_id}")

    # ... (rest of your code remains unchanged)

# About page
elif selected == "About":
    st.title("About Us")

    about_content = """
    <div class="about-container">
        <div class="about-section">
            <h2>Hi!, I am Devang Mestry</h2>
            <p>A Data Analyst from India</p>
            <div>
            </div>
            <p>I am passionate about finding ways to use Python and VBA to be more efficient in my work.</p>
        </div>
    </div>
    """

    st.markdown(about_content, unsafe_allow_html=True)

    # Use local CSS file
    with open("Landing_styles.css", "r") as f:
        css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Contact page
elif selected == "Contact":
    st.header(":mailbox: Get in Touch with us!")
    contact_form = """
        <form action="https://formsubmit.co/devangmestry3@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email"  placeholder="Your Email" required>  
            <textarea name="message" placeholder="Your Message here"></textarea>
            <button type="submit">Send</button>
        </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use local CSS file
    with open("FormStyle.css", "r") as f:
        css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Login page
elif selected == "Login":
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login Successful!")
            st.write("# Main Content Area")
            st.write("This is the main content area of your project.")
        else:
            st.error("Invalid username or password. Please try again.")

# Med-Bot page
elif selected == "Med-BOT":
    st.write("# Med-Bot")
st.write("## Ask your medical  questions here!")

st.title("")
client = OpenAI(api_key=st.secrets["OPEN_AI_API_KEY"])


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})