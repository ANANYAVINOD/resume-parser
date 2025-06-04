import streamlit as st
import os
from utils import extract_text_from_file, extract_email, extract_phone, extract_name
from skill_extractor import extract_skills

st.title("📄 Resume Parser & Skill Extractor")

uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    file_extension = uploaded_file.name.split('.')[-1]
    temp_file_path = f"temp_resume.{file_extension}"

    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        text = extract_text_from_file(temp_file_path)
        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)

        st.success("✅ Resume parsed successfully!")
        st.write("**👤 Name:**", name or "Not found")
        st.write("**📧 Email:**", email or "Not found")
        st.write("**📞 Phone:**", phone or "Not found")
        st.write("**💼 Skills:**", ', '.join(skills) if skills else "None detected")
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        os.remove(temp_file_path)
