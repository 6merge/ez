import sys
import os

# Add the parent directory to the system path to make 'mynk' package discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.gemini_client import gemini_ask


def generate_summary(text):
    """
    Generate a concise summary of the provided text (<= 150 words).
    Uses the Gemini API to summarize.
    """
    prompt = f"Summarize the following in 150 words:\n\n{text[:5000]}"
    return gemini_ask(prompt)

def answer_question(question, doc_text):
    """
    Answer a specific question based on the provided document text.
    Justify the answer with references to sections or quotes.
    """
    prompt = (
        f"Answer the following based only on this document:\n\n"
        f"{doc_text[:10000]}\n\nQuestion: {question}\n"
        f"Justify with reference to sections or quotes."
    )
    return gemini_ask(prompt)

def generate_logic_questions(doc_text):
    """
    Generate 3 logic-based or comprehension questions based on the document.
    """
    prompt = (
        f"Based on the following document, generate 3 logic-based or comprehension questions:\n\n{doc_text[:7000]}"
    )
    return gemini_ask(prompt)

def evaluate_user_answers(doc_text, questions, user_answers):
    """
    Evaluate the user's answers to the generated logic questions.
    Provide feedback and justification based on the document.
    """
    feedbacks = []
    for q, a in zip(questions, user_answers):
        prompt = (
            f"Document: {doc_text[:7000]}\n\n"
            f"Question: {q}\nUser's Answer: {a}\n"
            f"Evaluate the answer and provide justification from the document."
        )
        feedbacks.append(gemini_ask(prompt))
    return feedbacks
