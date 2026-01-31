import pytesseract
import cv2
import re
from datetime import datetime
import numpy as np
from datetime import datetime, timedelta


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# -----------------------------
# IMAGE PREPROCESSING FOR OCR
# -----------------------------
def preprocess_for_ocr(image_path):
    img = cv2.imread(image_path)

    # Resize to improve resolution
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # CLAHE — fixes uneven lighting
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    # Blur slightly to reduce noise
    gray = cv2.GaussianBlur(gray, (5,5), 0)

    # Adaptive threshold (better for curved surfaces)
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        31, 10
    )

    # Morphological closing to connect dotted characters
    kernel = np.ones((3,3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Remove tiny noise dots
    thresh = cv2.medianBlur(thresh, 3)

    return thresh




# -----------------------------
# OCR TEXT EXTRACTION
# -----------------------------
def extract_text(image_path):
    processed = preprocess_for_ocr(image_path)

    config = '--psm 6 -c tessedit_char_whitelist=0123456789./-'
    text = pytesseract.image_to_string(processed, config=config)


    print("OCR TEXT:", text)
    return text.lower()


# -----------------------------
# DATE EXTRACTION
# -----------------------------
def extract_expiry_date(text):
    """
    Supports:
    12/06/2025
    12.06.2025
    12-06-2025
    03 JUL 2009
    3 July 2009
    DEC 2003
    Dec-2026
    Aug 24
    """

    patterns = [
        r"\b\d{1,2}[./\s-]\d{1,2}[./\s-]\d{2,4}\b",  # numeric dates
        r"\b\d{1,2}\s?[A-Za-z]{3,9}\s?\d{2,4}\b",   # 03 JUL 2009
        r"\b[A-Za-z]{3,9}\s?\d{2,4}\b"               # DEC 2003
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group()

    return None



# -----------------------------
# CONVERT DATE TO DAYS LEFT
# -----------------------------
def expiry_to_days_left(date_str):
    date_str = date_str.strip()

    formats = [
        "%d/%m/%Y", "%d.%m.%Y", "%d-%m-%Y", "%d %m %Y",
        "%d %b %Y", "%d %B %Y",      # 03 Jul 2009
        "%b %Y", "%B %Y",            # Dec 2003
        "%b %y", "%B %y"             # Aug 24
    ]

    for fmt in formats:
        try:
            expiry_date = datetime.strptime(date_str, fmt)

            # If only month + year given, assume last day of month
            if "%d" not in fmt:
                next_month = expiry_date.replace(day=28) + timedelta(days=4)
                expiry_date = next_month - timedelta(days=next_month.day)

            today = datetime.now()
            delta = (expiry_date - today).days
            return max(delta, 0)
        except:
            continue

    return None
