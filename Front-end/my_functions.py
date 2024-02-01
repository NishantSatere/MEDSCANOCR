import cv2
import pytesseract
import re

def increase_font_size(image_path, output_path, font_size_multiplier):
    # Load the image
    img = cv2.imread(image_path)

    # Get image dimensions
    height, width, _ = img.shape

    # Define the font and other parameters
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = int(font_size_multiplier * 1.0)
    font_thickness = 2
    font_color = (255, 255, 255)

    # Position to place the text
    text_position = (int(width * 0.1), int(height * 0.9))

    # Increase the font size
    cv2.putText(img, "Sample Text", text_position, font, font_size, font_color, font_thickness)

    # Save the output image
    cv2.imwrite(output_path, img)

def extract_test_results(text):
    # Define patterns for extracting information
    patterns = {
        "Name": r"Name (.+)",
        "Lab No": r"Lab No\. (.+)",
        "Age": r"Age (\d+) Years",
        "Gender": r"Gender (.+)",
        "Collected": r"Collected: (.+)",
        "Reported": r"Reported (.+)",
        "Lab Status": r"Lab Status: (.+)",
        "Report Status": r"Report Status: (.+)",
        "Collected at": r"Collected at: (.+)",
        "Processed at": r"Processed at: (.+)",
        # Add more patterns as needed
    }

    # Initialize a dictionary to store extracted data
    data = {}

    # Extract information using patterns
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            data[key] = match.group(1).strip()

    # Updated regex pattern for test results
    test_results_pattern = r'(Hemoglobin|Packed Cell Volume \(PCV\)|REC Count|meV|NCH|NICHE|Red Call Distibution Width \(ROW\)|Total Leukocyte Count \(TLC\)|Differential Leucocyte Count \(DLC\)|Segmented Neutrophils|Lymphocytes|Monocytes|Eosinophils|Basophis|Absolute Leucocyte Count|Platelet Count|Mean Platelet Volume)\s+(\d+\.\d+|\d+)'

    # Extract test results
    test_results = re.findall(test_results_pattern, text)
    data["Test Results"] = [{"Test Name": result[0], "Result": result[1]} for result in test_results]

    return data
