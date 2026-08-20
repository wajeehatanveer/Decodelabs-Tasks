import cv2
import numpy as np
import pytesseract


def deskew_image(image):
    coords = np.column_stack(np.where(image == 0))

    if len(coords) == 0:
        return image

    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    height, width = image.shape[:2]
    center = (width // 2, height // 2)

    rotation_matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    deskewed = cv2.warpAffine(
        image,
        rotation_matrix,
        (width, height),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )

    return deskewed


def preprocess_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresholded = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    deskewed = deskew_image(thresholded)

    return deskewed


def extract_text(image):
    config = "--psm 6"

    data = pytesseract.image_to_data(
        image,
        config=config,
        output_type=pytesseract.Output.DICT
    )

    extracted_words = []

    for i in range(len(data["text"])):
        text = data["text"][i].strip()

        if not text:
            continue

        confidence = float(data["conf"][i])

        if confidence >= 80:
            extracted_words.append({
                "text": text,
                "confidence": confidence
            })

    return extracted_words


