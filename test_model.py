import streamlit as st
import pickle
from my_functions import increase_font_size, extract_test_results
import pytesseract
import cv2
import json
from pymongo import MongoClient

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit app title
st.title("Image Processing and Text Extraction App")

# File upload functionality
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "pdf"])

if uploaded_file is not None:
    # Read the content of the uploaded file
    image_content = uploaded_file.read()

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
    st.image(img, caption='Processed Image', use_column_width=True)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.text(text)

    # Extract information and convert to JSON
    patient_info = extract_test_results(text)
    json_data = json.dumps(patient_info, indent=2)
    json_dict = json.loads(json_data)
    
    # Display the JSON data
    st.subheader("Extracted Information (JSON):")
    st.json(patient_info)

    # Save the JSON data to MongoDB
    mongo_client = MongoClient("mongodb+srv://nishant-satere:nishant-satere-2810@firstproject.wami2av.mongodb.net/?retryWrites=true&w=majority")
    db = mongo_client["patient"]
    collection = db["patient"]

    # data_to_insert = 
        # json_dict  # Store only the JSON-formatted string
    

    # Insert data into MongoDB
    result = collection.insert_one(json_dict)
    st.success(f"Data saved to MongoDB with ObjectID: {result.inserted_id}")

    # Save data to pickle file (optional)
    # with open('saved_data.pkl', 'wb') as file:
    #     pickle.dump(json_dict, file)
