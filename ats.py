import os
import io
import base64
import streamlit as st
from PIL import Image
import pdf2image
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API"))

# ------------------------------ Utility Functions ------------------------------ #


def get_ai_response(input_text, image_bytes, prompt):
    """Send job description, resume image, and prompt to Gemini AI"""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([
        {"text": input_text},
        {"inline_data": {"mime_type": "image/jpeg", "data": image_bytes}},
        {"text": prompt}
    ])
    return response.text


def input_pdf(pdf_file):
    """Convert first page of uploaded PDF to JPEG bytes"""
    if pdf_file is None:
        raise FileNotFoundError("No resume uploaded")
    images = pdf2image.convert_from_bytes(pdf_file.read())
    img_bytes = io.BytesIO()
    images[0].save(img_bytes, format='JPEG')
    return img_bytes.getvalue()


# ------------------------------ Streamlit UI ------------------------------ #

st.set_page_config(page_title="ATS System", page_icon=":tada:", layout="wide")
st.header("AI-Powered Resume Analyser")

input_text = st.text_input("Enter Job Description", key="input_text")
pdf_file = st.file_uploader("Upload resume in PDF", type=["pdf"])

if pdf_file:
    st.success("✅ Resume uploaded successfully")

# Define buttons
submit1 = st.button("📄 Tell about resume")
submit2 = st.button("📈 How can I improve my skills")
submit3 = st.button("🔍 Keywords missing in resume")
submit4 = st.button("📊 Resume-job match %")

# ------------------------------ Prompts ------------------------------ #

input_prompt1 = """
You are an experienced technical HR professional with expertise in Data Science, 
Machine Learning, Full Stack Development,Big Data Engineering, DevOps, and Data Analytics.
Carefully review the resume and compare it with the job description.

Summarize the candidate’s:
- Professional experience
- Technical and soft skills
- Educational background
- Certifications or projects

Highlight the key strengths and areas of improvement.
"""

input_prompt2 = """
Act like a career coach. Analyze the resume and job description to:
- Identify missing skills/tools/technologies
- Recommend what to learn (e.g. Python, SQL, Docker)
- Suggest learning paths and project ideas
Return an actionable improvement plan.
"""

input_prompt3 = """
Act like an ATS system. Compare resume and job description to:
- Extract missing keywords (skills, tools, degrees, behaviors)
Return a clean bullet list with reasons why they matter for this role.
"""

input_prompt4 = """
Estimate job match percentage (0–100) based on:
- Skills match
- Experience match
- Education match
- Keyword presence

Break down the score like:
- Skill Match: XX%
- Experience Match: XX%
- Education Match: XX%
- Keyword Match: XX%

Then explain the reasoning briefly.
"""

# ------------------------------ Actions ------------------------------ #


def process_action(prompt):
    if not pdf_file:
        st.warning("⚠️ Please upload a resume first.")
        return
    image_bytes = input_pdf(pdf_file)
    result = get_ai_response(input_text, image_bytes, prompt)
    st.markdown(result)


if submit1:
    process_action(input_prompt1)
elif submit2:
    process_action(input_prompt2)
elif submit3:
    process_action(input_prompt3)
elif submit4:
    process_action(input_prompt4)

# ------------------------------ Footer ------------------------------ #

st.markdown("---")
st.markdown("<center>Powered by Gemini AI</center>", unsafe_allow_html=True)
