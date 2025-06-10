# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()


# Import necessary libraries
import os
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as generativeai
from google.generativeai.types import content_types
import base64
import io

# Configure the Gemini API using the key from environment variables
generativeai.configure(
    api_key=os.getenv("GOOGLE_API")
)


# Function to send the input text, resume image, and prompt to Gemini AI and get response
def get_ai_response(input_text, image_bytes, prompt):
    model = generativeai.GenerativeModel('gemini-1.5-flash')


    # Send input as list of content parts (text + image + prompt)
    response = model.generate_content([
        {"text": input_text},
        {"inline_data": {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }},
        {"text": prompt}
    ])

    return response.text

# Function to convert first page of uploaded PDF to JPEG image bytes
def input_pdf(pdf_file):
    if pdf_file is None:
        raise FileNotFoundError("File is not found")

    # Convert PDF to image
    image_list = pdf2image.convert_from_bytes(pdf_file.read())
    first_page = image_list[0]

    # Convert image to bytes (JPEG)
    img_bytes = io.BytesIO()
    first_page.save(img_bytes, format='JPEG')
    return img_bytes.getvalue()




# Streamlit Page Configuration
st.set_page_config(
    page_title="ATS System",
    page_icon=":tada:",
    layout="wide"
)


# UI Title
st.header("ATS System")

# Job description input
input_text=st.text_input("Enter Job Description", key="input_text")

# Resume file upload input
pdf_file=st.file_uploader("Upload resume in PDF", type=["pdf"])

# Confirmation message if resume is uploaded
if pdf_file is not None:
    st.write("Resume uploaded successfully")

submit1=st.button("Tell about resume")
submit2=st.button("How can i improve my skills")
submit3=st.button("Tell Important Keyword that are missing in resume")
submit4=st.button("Percentage match")

# Prompt 1: Resume summary and evaluation by HR
input_prompt1 = """
You are an experienced technical HR professional with tech experience in field of Data Science, Full stack development, Big Data Enginering, DEVOPS, Data Analyst and resume evaluator. Carefully review the provided resume and compare it against the job description.
Summarize the candidate’s key qualifications, including their:
- Professional experience
- Technical and soft skills
- Educational background
- Certifications or projects (if any)

Your analysis should highlight areas where the candidate aligns well with the job role, and areas that stand out as strengths.
Provide a clear, concise summary as if you were briefing a recruiter or hiring manager.
Highlight the strengths and weaknesses of the candidate in relation to the specified
requirements for the job."""


# Prompt 2: Improvement suggestions for skills based on resume
input_prompt2 = """
You are acting as a career coach. Analyze the resume in the context of the given job description.
Identify the specific skills, tools, technologies, or experience areas that the candidate is currently lacking or should strengthen to become a stronger match for the position.

Your suggestions should be:
- Role-specific (e.g., for a data analyst: Python, SQL, Power BI)
- Practical (e.g., learn XYZ through projects or online platforms)
- Based on gaps between the resume and job description

Present your answer as an actionable improvement plan the candidate can follow.
"""

# Prompt 3: Extract missing keywords in the resume
input_prompt3 = """
You are functioning as an Applicant Tracking System (ATS). Compare the resume content with the job description and identify:
- Important keywords (technical terms, tools, role-specific jargon)
- Certifications or educational terms
- Soft skills or behavioral traits

List the keywords and concepts that are present in the job description but missing in the resume. These keywords are often used by ATS software to rank applicants, so be precise and focused.

Format the output as a list, and optionally explain why each keyword might be important for this role.
"""

# Prompt 4: Calculate and explain resume-job match percentage
input_prompt4 = """
You are a resume screening assistant trained to estimate job match percentages. Carefully review the resume and compare it against the job description.

Provide a score out of 100 representing how well the candidate matches the role based on:
- Skills match
- Experience relevance
- Educational qualifications
- Use of role-relevant keywords

After calculating the match score, explain the reasoning behind your percentage.
Also, include a breakdown like:
- Skill Match: XX%
- Experience Match: XX%
- Education Match: XX%
- Keyword Match: XX%

Be objective, concise, and helpful.
"""

# Handle "Tell about resume" button click
if submit1:
    if pdf_file is None:
        st.write("Please upload resume")
    else:
        image_bytes = input_pdf(pdf_file)
        ai_response = get_ai_response(input_text, image_bytes, input_prompt1)
        st.write(ai_response)

# Handle "How can I improve my skills" button click
if submit2:
    if pdf_file is None:
        st.write("Please upload resume")
    else:
        image_bytes = input_pdf(pdf_file)
        ai_response = get_ai_response(input_text, image_bytes, input_prompt2)
        st.write(ai_response)

# Handle "Tell Important Keyword that are missing in resume" button click
if submit3:
    if pdf_file is None:
        st.write("Please upload resume")
    else:
        image_bytes = input_pdf(pdf_file)
        ai_response = get_ai_response(input_text, image_bytes, input_prompt3)
        st.write(ai_response)

# Handle "Percentage match" button click
if submit4:
    if pdf_file is None:
        st.write("Please upload resume")
    else:
        image_bytes = input_pdf(pdf_file)
        ai_response = get_ai_response(input_text, image_bytes, input_prompt4)
        st.write(ai_response)
