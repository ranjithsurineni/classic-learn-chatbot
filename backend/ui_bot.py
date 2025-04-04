import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

#----------for--ui------------
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

# Initialize Rich console
console = Console()

# Load FAQ data from external JSON file
def load_faq_data(filename="data01.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# Load training data (FAQs or predefined Q&A pairs) for Classic Learn
data = load_faq_data()

# Extract questions and answers
questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Convert text data into numerical form using TF-IDF vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_answer(user_query):
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vector, question_vectors).flatten()
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]

    if best_match_score > 0.5:
        return answers[best_match_index]

    # Extract keywords from user query
    user_keywords = set(re.findall(r'\w+', user_query.lower()))
    best_match = "I'm sorry, I couldn't find an exact answer. Please visit our website for more details."
    max_overlap = 0

    for idx, question in enumerate(questions):
        question_keywords = set(re.findall(r'\w+', question.lower()))
        overlap = len(user_keywords & question_keywords)

        if overlap > max_overlap:
            max_overlap = overlap
            best_match = answers[idx]

    return best_match

# Interactive chatbot loop with advanced terminal UI
if __name__ == "__main__":
    console.print(Panel("Welcome to the [bold blue]Classic Learn Chatbot[/bold blue]!", title="🤖 Chatbot", subtitle="Your Learning Assistant"))
    console.print("Type 'exit' to stop the conversation.", style="bold green")
    console.print("=" * 50, style="bold yellow")

    while True:
        user_input = Prompt.ask("[bold cyan]You[/bold cyan]")
        if user_input.lower() == "exit":
            console.print(Panel("[bold red]Goodbye![/bold red] Have a great day!", title="👋 Chatbot"))
            break
        response = get_answer(user_input)
        console.print(Panel(Text(response, style="bold white"), title="🤖 Chatbot"))