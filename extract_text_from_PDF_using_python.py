import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

BASE_PATH = r"E:\projectswithpython"
POPPLER_PATH = r"C:\poppler\poppler-25.12.0\Library\bin"
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

pdf_files = [
    f for f in os.listdir(BASE_PATH)
    if f.lower().endswith(".pdf")
]

def pdf_extract(pdf_file, index):
    print("Extracting from:", pdf_file)

    pdf_path = os.path.join(BASE_PATH, pdf_file)

    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    result_path = os.path.join(BASE_PATH, f"result{index}.txt")

    with open(result_path, "w", encoding="utf-8") as out:
        for page_no, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            out.write(f"\n\n--- Page {page_no + 1} ---\n")
            out.write(text)

for i, pdf in enumerate(pdf_files):
    pdf_extract(pdf, i)
