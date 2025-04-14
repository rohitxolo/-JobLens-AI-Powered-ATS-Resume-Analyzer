from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64
import io

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("JobLens")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 =  """
You are an experienced and detail-oriented Technical Human Resource Manager.

Your task is to critically analyze the provided resume and evaluate its alignment with the given job description.

Please provide a professional assessment that includes:
1. **Overall Fit** - How well does the candidate meet the job requirements?
2. **Key Strengths** - Highlight the skills, experiences, or achievements that strongly match the job description.
3. **Gaps or Weaknesses** - Identify any missing qualifications, skills, or mismatches that could affect suitability.
4. **Recommendation** - Would you shortlist this candidate for an interview? Justify your decision.

Ensure your response is clear, objective, and based solely on the provided resume and job description.
"""


input_prompt3 = """
You are an advanced Applicant Tracking System (ATS) with in-depth knowledge of data science roles and recruitment analysis. 
Your task is to analyze the candidates resume against the provided job description and return the following in order:

1. **Match Percentage**: Provide a percentage score indicating how well the resume aligns with the job description.
2. **Missing Keywords**: List important skills, tools, or qualifications present in the job description but missing from the resume.
3. **Final Evaluation**: Offer a concise summary of your assessment, including the candidate’s potential fit for the role and any significant gaps.

Ensure the evaluation is accurate, objective, and clearly formatted.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



   




