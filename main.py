from config import chain
import os


# Function to load text from a file
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()


# Function to get similarity score from LLM
def get_answer(question):
    # Run the LLM chain with the given inputs
    response = chain.invoke({
        "question": question
    })

    # Parse and return the similarity score
    try:
        ans = response.content.strip()
        return ans
    except ValueError:
        raise ValueError("The model did not return a valid score.")


# Example usage
if __name__ == "__main__":
    # Load content from files
    question = load_text_from_file(os.path.join(
        os.path.dirname(__file__), 'question.txt'))

    answer = get_answer(question)
    print(f"{answer}")