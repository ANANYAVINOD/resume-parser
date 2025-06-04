from utils import extract_text_from_file, extract_email, extract_phone, extract_name
from skill_extractor import extract_skills

resume_path = 'resumes/sample_resume.pdf'  # Replace with your own resume file path

text = extract_text_from_file(resume_path)

parsed_data = {
    "Name": extract_name(text),
    "Email": extract_email(text),
    "Phone": extract_phone(text),
    "Skills": extract_skills(text)
}

for key, value in parsed_data.items():
    print(f"{key}: {value}")