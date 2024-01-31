from PIL import Image
import pytesseract
import re
import json

def extract_information(text):
    extracted_data = {}

    # Extract patient name
    patient_name_pattern = r'Name (.+?) Collected'
    patient_name_match = re.search(patient_name_pattern, text)
    if patient_name_match:
        extracted_data['Name'] = patient_name_match.group(1).strip()

    # Extract age
    age_pattern = r'Age: \'(\d+) Years'
    age_match = re.search(age_pattern, text)
    if age_match:
        extracted_data['Age'] = int(age_match.group(1))

    # Extract gender
    gender_pattern = r'Gender: (.+?) Reported'
    gender_match = re.search(gender_pattern, text)
    if gender_match:
        extracted_data['Gender'] = gender_match.group(1).strip()

    # Extract lab results
    lab_results_pattern = r'Test Name Results Units Bio\. Ref\. Interval(.+?)\n\n'
    lab_results_match = re.search(lab_results_pattern, text, re.DOTALL)
    if lab_results_match:
        lab_results_section = lab_results_match.group(1).strip()
        extracted_data['LabResults'] = extract_lab_results(lab_results_section)

    return extracted_data

def extract_lab_results(lab_results_section):
    lab_results = []

    # Extract test names and results
    test_results_pattern = r'(\w+.*?)\s+(\S+)\s+(\S+)\s+(\S+)'
    test_results_matches = re.finditer(test_results_pattern, lab_results_section)

    for match in test_results_matches:
        test_name = match.group(1).strip()
        result = match.group(2).strip()
        units = match.group(3).strip()
        reference_interval = match.group(4).strip()

        lab_result = {
            'TestName': test_name,
            'Result': result,
            'Units': units,
            'ReferenceInterval': reference_interval
        }
        lab_results.append(lab_result)

    return lab_results

def ocr_image_and_extract(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    # Extract information and format as JSON
    extracted_data = extract_information(text)
    json_data = json.dumps(extracted_data, indent=2)

    return json_data

# Example usage
image_path = 'img1.jpg'
json_result = ocr_image_and_extract(image_path)
print("Extracted Data (JSON):")
print(json_result)
