from transformers import pipeline

qa_pipeline = pipeline("question-answering")
gen_pipeline = pipeline("text-generation", model="gpt2")

def ask_question(context, question):
    result = qa_pipeline(question=question, context=context)
    return result['answer'], f"Found in context: \"{result['answer']}\""

def generate_challenge_questions(document_text):
    prompt = f"Generate 3 logic or comprehension questions based on the document:\n{document_text[:1000]}"
    response = gen_pipeline(prompt, max_length=300, num_return_sequences=1)[0]['generated_text']
    questions = [q.strip() for q in response.split("?") if q.strip()]
    return [{"question": q + "?", "answer": "Answer derived manually or using QA"} for q in questions[:3]]

def evaluate_user_answer(user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.strip().lower():
        return "✅ Correct!"
    return f"❌ Incorrect. Correct Answer: {correct_answer}"
