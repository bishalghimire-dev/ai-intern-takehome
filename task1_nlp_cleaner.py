import json
import re
from collections import Counter


# PART 1: DATA CLEANING

def clean_tickets(tickets):

    cleaned_tickets = []
    seen_ids = set()

    for ticket in tickets:

        ticket_id = ticket.get("ticket_id")
        query = ticket.get("query")

        # Skip duplicate tickets
        if ticket_id in seen_ids:
            continue

        seen_ids.add(ticket_id)

        # Skip invalid or empty queries
        if not isinstance(query, str) or not query.strip():
            continue

        # Remove HTML tags
        query = re.sub(r'<[^>]+>', '', query)

        # Remove unnecessary spaces
        query = query.strip()

        ticket["query"] = query

        cleaned_tickets.append(ticket)

    return cleaned_tickets


# PART 2: NLP PREPROCESSING

def preprocess_text(text):

    stop_words = {
        "the", "is", "on", "and", "do", "i", "my",
        "to", "from", "or", "can", "how", "what",
        "after", "a", "an", "are", "in", "of",
        "for", "it", "with", "all", "me", "they",
        "their", "get", "be"
    }

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Tokenization
    words = text.split()

    # Remove stop words
    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    return filtered_words

def analyze_tickets(cleaned_tickets):

    category_counts = Counter()
    keyword_counts = Counter()

    processed_tickets = []

    for ticket in cleaned_tickets:

        category = ticket.get("category", "Unknown")
        category_counts[category] += 1

        tokens = preprocess_text(ticket["query"])
        keyword_counts.update(tokens)

        processed_ticket = ticket.copy()
        processed_ticket["tokens"] = tokens

        processed_tickets.append(processed_ticket)

    print("\nTickets per category:")
    print(dict(category_counts))

    print("\nTop 5 frequent keywords:")

    for word, count in keyword_counts.most_common(5):
        print(f"{word}: {count}")

    with open("data/cleaned_tickets.json", "w", encoding="utf-8") as file:
        json.dump(processed_tickets, file, indent=4)

    print("\nCleaned tickets saved successfully!")

    # MAIN PROGRAM

if __name__ == "__main__":

    with open("data/support_tickets.json", "r", encoding="utf-8") as file:
        tickets = json.load(file)

    cleaned_tickets = clean_tickets(tickets)

    print("Original tickets:", len(tickets))
    print("Valid cleaned tickets:", len(cleaned_tickets))

    analyze_tickets(cleaned_tickets)