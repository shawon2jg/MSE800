import streamlit as st
import openai
from utils import extract_text

st.set_page_config(page_title="Resume Scanner", page_icon="🔍")

st.title("🔍 Resume Scanner")
st.write("Upload your resume and let AI analyze it!")

# Sidebar
st.sidebar.header("Select provider")
provider = st.sidebar.radio("Choose provider:", ["OpenAI", "Google Generative AI"])
st.sidebar.markdown("---")

# API key input
if provider == "OpenAI":
    openai.api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
else:
    st.sidebar.text_input("Enter your Google AI Key", type="password")

# File upload
uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF, DOCX, or TXT)",
    type=["pdf", "docx", "txt"],
    help="Upload your CV file to get started."
)

if uploaded_file is not None:
    file_type = uploaded_file.type
    resume_text = extract_text(uploaded_file, file_type)

    if resume_text:
        st.subheader("Resume Preview")
        st.text_area("Extracted Resume Text", resume_text[:1500] + "..." if len(resume_text) > 1500 else resume_text,
                     height=300)

        if st.button("Analyze Resume"):
            with st.spinner("Analyzing your resume... ⏳"):
                prompt = f"""
                You are a professional career assistant.
                Analyze the following resume text:
                {resume_text}

                Provide the following insights:
                1. Candidate Summary
                2. Key Skills
                3. Strengths and Weaknesses
                4. Job Role Recommendations
                5. Overall Impression
                """

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7
                    )
                    analysis = response["choices"][0]["message"]["content"]
                    st.success("✅ Analysis Complete!")
                    st.write(analysis)
                except Exception as e:
                    if "quota" in str(e).lower():
                        st.error(
                            "⚠️ Your OpenAI API quota has been exceeded. Please check your billing or API key at https://platform.openai.com/account/billing")
                    else:
                        st.error(f"Unexpected error: {e}")
    else:
        st.error("Could not extract text from the uploaded file.")
