import streamlit as st
from document_processor import process_file, generate_summary
from qa_module import ask_question, generate_challenge_questions, evaluate_user_answer

st.title("🧠 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])
if uploaded_file:
    st.success("File uploaded successfully!")

    text = process_file(uploaded_file)
    summary = generate_summary(text)
    st.subheader("🔍 Auto Summary")
    st.write(summary)

    mode = st.radio("Choose a mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Ask a question based on the document")
        if question:
            answer, justification = ask_question(text, question)
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"_Justification:_ {justification}")

    elif mode == "Challenge Me":
        st.subheader("🤖 Here are your questions:")
        questions = generate_challenge_questions(text)
        user_answers = []
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Q{i}: {q['question']}**")
            user_input = st.text_input(f"Your Answer to Q{i}", key=i)
            if user_input:
                feedback = evaluate_user_answer(user_input, q["answer"])
                st.write(feedback)
