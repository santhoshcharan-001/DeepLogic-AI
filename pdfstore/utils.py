from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"


def extract_text(pdfFile):
    pages = convert_from_path(
        pdfFile, 500, poppler_path=r"C:\Users\Ki\Downloads\poppler-0.68.0_x86\poppler-0.68.0\bin"
    )

    text = ""
    print("Total pages: ", len(pages))
    for page in pages:
        # Extract text from each page
        text += pytesseract.image_to_string(page)
    print(text)
    return text
