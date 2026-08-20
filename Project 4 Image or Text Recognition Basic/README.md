# Project 4: Building the Machine's Optic Nerve

### The DecodeLabs Architect's Playbook for Image & Text Recognition

## 📌 Project Overview

This project implements a basic Optical Character Recognition (OCR) system that extracts text from images using OpenCV and Tesseract OCR.

The system preprocesses an uploaded image before performing OCR to improve text recognition.

## 🎯 Objectives

- Accept an image as input
- Preprocess the image using OpenCV
- Convert the image to grayscale
- Apply Gaussian Blur
- Apply Adaptive Thresholding
- Perform image deskewing
- Extract text using Tesseract OCR
- Display confidence scores
- Filter OCR results using an 80% confidence threshold
- Provide a simple Streamlit interface

## 🔄 OCR Pipeline

```text
Image Input
     ↓
Grayscale
     ↓
Gaussian Blur
     ↓
Adaptive Thresholding
     ↓
Deskewing
     ↓
Tesseract OCR
     ↓
Confidence Filtering (80%+)
     ↓
Extracted Text
````

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* Pytesseract
* Tesseract OCR
* Streamlit

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Tesseract OCR must also be installed separately on Windows.

After installation, verify it with:

```bash
tesseract --version
```

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application allows the user to upload an image and extract text using OCR.

## 🖼️ Supported Image Formats

The application supports:

* PNG
* JPG
* JPEG
* WEBP
* JFIF

## 📊 Confidence Filtering

Only OCR results with a confidence score of **80% or higher** are displayed in the extracted text section.

Confidence scores are also displayed separately for the recognized words.

## 🧪 Testing

The application was tested using sample text images to verify:

* Image preprocessing
* OCR text extraction
* Confidence scoring
* 80% confidence filtering
* Streamlit interface

## 📌 Project Path

This project follows **Path 1: OCR — Extract text from images**.

Object detection is not included because it belongs to the alternative project path.

## 👩‍💻 Project

**DecodeLabs Internship — Project 4**

**Project:** Image or Text Recognition (Basic)
