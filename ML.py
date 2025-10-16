import cv2
import easyocr
import numpy as np
import re

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to preprocess image
def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # Resize for better recognition
    _, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)  # Binarization
    kernel = np.ones((2, 2), np.uint8)
    processed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # Noise removal
    return processed

# Function to extract text using EasyOCR
def extract_equation(image_path):
    processed_image = preprocess_image(image_path)
    results = reader.readtext(processed_image, detail=0)  # Extract text
    text = ' '.join(results)  # Combine recognized text
    return text.strip()

# Function to evaluate equation
def solve_equation(equation):
    equation = re.sub(r'[^0-9+\-*/().]', '', equation)  # Remove unwanted characters
    try:
        result = eval(equation)
        return result
    except Exception as e:
        return f"Error solving equation: {e}"

if __name__ == "__main__":
    image_path = "image-path"  # Update with your image file path
    equation = extract_equation(image_path)
    print(f"Extracted Equation: {equation}")
    result = solve_equation(equation)
    print(f"Solution: {result}")