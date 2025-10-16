Handwritten Equation Solver using EasyOCR and OpenCV

This project automatically extracts and solves handwritten mathematical equations from images using EasyOCR and OpenCV.
It leverages Optical Character Recognition (OCR) to detect and interpret handwritten text, preprocesses the image for better accuracy, and then evaluates the extracted mathematical expression.

Features:
Image-based Equation Recognition — Reads handwritten equations from images.
OCR using EasyOCR — Detects handwritten characters efficiently.
Image Preprocessing with OpenCV — Enhances image clarity using grayscale conversion, binarization, and noise removal.
Automatic Equation Evaluation — Parses and computes mathematical results using Python’s built-in eval() safely.
Lightweight & Easy to Run — Works locally with minimal setup.

Technologies Used:
Python 3.x
OpenCV — For image preprocessing (grayscale, thresholding, morphological operations).
EasyOCR — For extracting handwritten text.
NumPy — For array and image manipulation.
re (Regex) — For cleaning the extracted equation before evaluation.
