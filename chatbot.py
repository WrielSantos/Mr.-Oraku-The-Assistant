import openai

# Set your API key
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

# Custom response logic for High School English Language Arts, tailored for ELLs
system_message = "You are an assistant for High School English Language Arts, skilled in assisting English Language Learners. Provide simplified explanations and align with Common Core Standards."

def chat_with_openai(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use text-davinci-002 engine
            prompt=system_message + prompt,
            max_tokens=50  # Adjust based on your requirements
        )
        content = response['choices'][0]['text']

        # Guiding Students to Answers, considering ELLs
        if any(keyword in prompt.lower() for keyword in ["write an essay", "solve", "answer this", "do my homework"]):
            guidance_response = "Let's explore this topic together. Can you tell me what you understand so far, and what specific aspect you're finding challenging?"
            return guidance_response
        else:
            # Simplify language for ELLs
            content = simplify_language_for_ells(content)
            return content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generate_quiz():
    # ELA-specific quiz questions aligned with High School Common Core Standards
    quiz_questions = [
        "Analyze the use of imagery in Edgar Allan Poe's 'The Raven'.",
        "Compare and contrast the themes in '1984' by George Orwell and 'Brave New World' by Aldous Huxley.",
        "Identify the main argument in Martin Luther King Jr.'s 'I Have a Dream' speech.",
        "Explain the significance of the first-person narrative in 'The Catcher in the Rye'."
    ]

    return random.choice(quiz_questions)

def simplify_language_for_ells(text):
    # Placeholder function to simplify language; in practice, this would use NLP techniques
    # to simplify sentence structure and vocabulary for ELLs
    # For now, this is just a conceptual representation.
    return text  # Implement language simplification logic here

# Example usage
prompt = "Explain the symbolism in 'The Great Gatsby'."
response = chat_with_openai(prompt)
print(response)

# Generating a quiz question (make sure to import 'random' if not already imported)
import random
quiz_question = generate_quiz()
print(f"Quiz Question: {quiz_question}")

# Feedback mechanism (keep this if you want to collect feedback)
feedback = input("Was this response helpful? (Yes/No): ")
print(f"Thank you for your feedback: {feedback}")
