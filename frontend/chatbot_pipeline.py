import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json



def load_faq_data(filename="data01.json"):
    """Loads FAQ data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


# Load FAQ Data
data = load_faq_data()
questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]



# Convert text data into numerical form using TF-IDF
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

'''
def get_answer(user_query):
    """Returns the best matching answer for a user query."""
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vector, question_vectors).flatten()
    
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]
    
    if best_match_score > 0.5:
        return answers[best_match_index]
    
    # Keyword Matching Fallback
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
'''


def find_best_match(user_query):
    """Finds the best matching answer for a user query."""
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vector, question_vectors).flatten()
    
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]
    
    if best_match_score > 0.5:
        return answers[best_match_index]
    
    # Keyword Matching Fallback
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
