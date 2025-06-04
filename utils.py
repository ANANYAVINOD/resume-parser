import re
import docx2txt
from pdfminer.high_level import extract_text

def extract_text_from_file(file_path):
    if file_path.endswith('.pdf'):
        return extract_text(file_path)
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format")

def extract_email(text):
    match = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3})?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}', text)
    return match.group() if match else None

def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines:
        words = line.split()
        if len(words) >= 2 and all(w[0].isupper() for w in words[:2]):
            return ' '.join(words[:2])
    return None
