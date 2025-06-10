# Import necessary libraries
import os
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as generativeai
from google.generativeai.types import content_types

# Configure the Generative AI API with the API key from the environment variable
generativeai.configure(
    api_key=os.getenv("GOOGLE_API")
)

# Define a function to get a response from the AI model
def get_ai_response(input_text, image_bytes, prompt):
    """
    Get a response from the Generative AI model.

    Args:
        input_text (str): The input text to the model.
        image_bytes (bytes): The image bytes to include in the model input.
        prompt (str): The prompt to use for the model.

    Returns:
        str: The response from the model.
    """
    # Create a GenerativeModel instance with the 'gemini-1.5-flash' model
    model = generativeai.GenerativeModel('gemini-1.5-flash')

    # Generate content using the model with the input text, image bytes, and prompt
    response = model.generate_content([
        {"text": input_text},
        {"inline_data": {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }},
        {"text": prompt}
    ])

    # Return the text response from the model
    return response.text

# Define a function to input a PDF file and convert it to an image
def input_pdf(pdf_file):
    """
    Input a PDF file and convert it to an image.

    Args:
        pdf_file: The PDF file to input.

    Returns:
        bytes: The image bytes from the first page of the PDF.

    Raises:
        FileNotFoundError: If the PDF file is not found.
    """
    # Check if the PDF file is None
    if pdf_file is None:
        raise FileNotFoundError("File is not found")

    # Convert the PDF file to a list of images using pdf2image
    image_list = pdf2image.convert_from_bytes(pdf_file.read())

    # Get the first page of the PDF as an image
    first_page = image_list[0]

    # Create a BytesIO instance to store the image bytes
    img_bytes = io.BytesIO()

    # Save the image to the BytesIO instance in JPEG format
    first_page.save(img_bytes, format='JPEG')

    # Return the image bytes
    return img_bytes.getvalue()

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="ATS System",
    page_icon=":tada:",
    layout="wide"
)

# Set the header for the Streamlit app
st.header("ATS System")