import fitz  # PyMuPDF
import os

def extract_text(file_path: str) -> str:
    """Extract text from PDF or TXT file."""
    # Check if it's a PDF file
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    
    # Check if it's a TXT file
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or TXT file.")

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)  # Open the PDF file
    text = ""
    for page in doc:
        text += page.get_text()  # Extract text from each page
    return text

def extract_text_from_txt(txt_path: str) -> str:
    """Extract text from a TXT file."""
    with open(txt_path, "r", encoding="utf-8") as file:
        return file.read()  # Read the entire content of the TXT file
