# 📄 JobLens – AI-Powered ATS Resume Analyzer

JobLens is an AI-powered resume analysis tool that mimics an Applicant Tracking System (ATS). Built using **Streamlit** and **Google Gemini**, it helps job seekers, especially freshers, evaluate how well their resumes align with a given job description. It provides match percentage, missing keywords, and detailed professional feedback.

---

## 🚀 Features

- ✅ Upload resume in PDF format
- 🧠 Uses Google Gemini 1.5 Flash model for analysis
- 📊 ATS-style percentage match with job description
- 🔍 Highlights missing keywords/skills
- ✍️ Provides professional HR-style evaluation
- 🖼️ Converts PDF to image for LLM compatibility

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 1.5 Flash (via API)
- **PDF/Image**: pdf2image, Pillow
- **Env Management**: python-dotenv

---


## 🧪 How It Works

- Enter the Job Description (e.g., Software Developer – Fresher).

- Upload your Resume (PDF).

- Click one of the buttons:

- Tell Me About the Resume – Detailed HR-style feedback

- Percentage Match – ATS match %, missing keywords, and evaluation

- Review the AI-generated response on the screen.

---

## 📄 Sample Job Description (SDE – Fresher)
We are looking for a Software Development Engineer (SDE) who is passionate about technology and innovation. 
The ideal candidate should have strong programming skills in languages like Python, Java, or C++, a good grasp of data structures and algorithms,
and familiarity with web technologies or databases...

---

## 🤖 Prompt Engineering
🔹 HR-Style Prompt

Critically analyze the resume for strengths, weaknesses, and recommend if the candidate should be shortlisted.

🔹 ATS-Style Prompt

Calculate match percentage, identify missing skills, and provide a final evaluation.

---

## ✅ To Do / Future Improvements
- 🔍 OCR for full resume content

- 📊 Visualize skill match using charts

- 📄 Support multi-page resume evaluation

- 🤖 Suggest resume improvements with AI

---

## 👨‍💻 Author
Made with ❤️ by GEDELA ROHIT CHANDRA
