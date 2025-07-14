import streamlit as st
from utils.qa_logic import generate_summary, answer_question, generate_logic_questions, evaluate_user_answers
import os
from PIL import Image

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F4F7FA;
            color: #333;
        }

        .stButton>button {
            background-color: #00A8CC;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 20px;
            transition: background-color 0.3s ease-in-out;
            border: 2px solid #00A8CC;
        }
        
        .stButton>button:hover {
            background-color: #007B8F;
        }

        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #DDD;
        }

        .stTextInput>div>div>input:focus {
            border: 2px solid #00A8CC;
        }

        .stFileUploader>div>div>input[type=file] {
            font-size: 16px;
            background-color: #ffffff;
            padding: 10px;
            border: 1px solid #DDD;
            border-radius: 5px;
        }

        .stText {
            font-size: 18px;
            font-weight: 400;
        }

        .stMarkdown {
            font-size: 18px;
            font-weight: 300;
            color: #555;
        }

        .section-title {
            font-size: 22px;
            font-weight: 700;
            color: #00A8CC;
        }

        .output-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            border: 2px solid #DDD;  /* Added border */
        }

        .upload-area {
            padding: 40px 20px;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            border: 2px solid #DDD;  /* Added border */
        }

        .section-box {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            border: 2px solid #DDD;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        .footer {
            text-align: center;
            padding: 20px;
            background-color: #f7f7f7;
            border-top: 1px solid #DDD;
        }
    </style>
    """, unsafe_allow_html=True)

# Title and Introduction
st.title("Smart Research Assistant")
st.markdown("""
    This AI assistant helps you quickly analyze and summarize long documents such as research papers, legal files, or technical manuals.
    Simply upload your document, ask questions, or challenge yourself with comprehension questions.
    """)

# Upload section with border
st.markdown('<div class="section-title">Upload Document</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file is not None:
    # Display document upload status
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # Extract text from document
    file_extension = uploaded_file.name.split('.')[-1]
    if file_extension == "pdf":
        # Handle PDF (add the extraction code for PDF here)
        st.markdown('<div class="section-title">Extracting Text...</div>', unsafe_allow_html=True)
        # You would add your text extraction logic here
        st.session_state.doc_text = "Extracted text from PDF (example text)"
    elif file_extension == "txt":
        text = uploaded_file.read().decode("utf-8")
        st.session_state.doc_text = text

    # Show auto-summary with border
    st.markdown('<div class="section-title">Document Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    summary = generate_summary(st.session_state.doc_text)
    st.write(summary)
    st.markdown('</div>', unsafe_allow_html=True)

    # Interaction Mode: Ask Anything
    st.markdown('<div class="section-title">Ask Anything</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    question = st.text_input("Ask your question:")
    if question:
        answer = answer_question(question, st.session_state.doc_text)
        st.markdown(f"**Answer:** {answer}")
        st.markdown("Justification: Based on document content.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Interaction Mode: Challenge Me
    st.markdown('<div class="section-title">Challenge Me</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    challenge_button = st.button("Generate Challenge Questions")
    if challenge_button:
        questions = generate_logic_questions(st.session_state.doc_text)
        st.markdown("**Generated Questions:**")
        for idx, question in enumerate(questions, start=1):
            st.markdown(f"**Q{idx}:** {question}")

        # Get user answers
        user_answers = []
        for idx in range(1, len(questions) + 1):
            user_answer = st.text_area(f"Your answer to Q{idx}")
            user_answers.append(user_answer)

        # Evaluate answers
        if st.button("Evaluate Answers"):
            feedbacks = evaluate_user_answers(st.session_state.doc_text, questions, user_answers)
            for idx, feedback in enumerate(feedbacks, start=1):
                st.markdown(f"**Feedback for Q{idx}:** {feedback}")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer with Github link
st.markdown("""
    <div class="footer">
        <p>For more details, visit my GitHub: <a href="https://github.com/6merge" target="_blank">GitHub Profile</a></p>
    </div>
    """, unsafe_allow_html=True)
