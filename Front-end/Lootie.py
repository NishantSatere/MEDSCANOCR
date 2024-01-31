import streamlit as st
import requests

# Function to load Lottie animation from URL
st.set_page_config(page_title="My WebPage",page_icon=" :tada: ",layout="wide")


#Heading Section
with st.container():
    st.subheader("Hi!, I am Devang Mestry")
    st.title("A Data Analyst from India")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient  in my work.") 
    st.write("[Learn More >]")
    
    with st.container():
        st.write("---")
        left_column,right_column=st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            
            st.write(
                """
MedScanOCR revolutionizes medical document management by seamlessly integrating 
cutting-edge OCR capabilities, structured data conversion, user-friendly interfaces,
and intelligent chatbot integration. Our robust OCR engine accurately extracts text from medical
records in various formats, ensuring precision and reliability. The extracted data is then converted
into a structured JSON key-value format, enhancing integrity and relevance. With an intuitive interface
supporting document upload via camera or file upload, users can effortlessly organize multiple 
pages by test name and dates. MedScanOCR's dual interfaces enable dynamic data querying and retrieval
, empowering users to access specific information with ease. The intelligent chatbot further streamlines
operations by facilitating document data queries, such as retrieving Red Blood Cell (RBC) counts chronologically 
from all reports. With MedScanOCR, medical professionals experience unprecedented efficiency, accuracy,
and convenience in managing diagnostic reports.
                """
            )

import streamlit as st
with open("Landing_styles.css", "r") as f:
        css_content = f.read()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Load CSS

# Display text with image aligned to the right
st.markdown("""
    <div class="image-container">
        <div>
            <p>1. MedScanOCR integrates OCR capabilities for accurate text extraction from medical records.</p>
            <p>2. It converts extracted text data into structured JSON format, ensuring integrity and relevance.</p>
            <p>3. The user-friendly interface allows easy document upload via camera or file upload.</p>
            <p>4. Dual interfaces enable seamless document upload and dynamic data querying.</p>
            <p>5. Intelligent chatbot integration facilitates efficient retrieval of specific information from reports.</p>
        </div>
        <img src="heydr.jpg" alt="Image" />
    </div>
""", unsafe_allow_html=True)
