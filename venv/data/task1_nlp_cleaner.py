import json
import re
from collections import Counter

def clean_tickets(tickets):

    cleaned_tickets = []
    seen_ids = set()

    for ticket in tickets:

        ticket_id = ticket.get("ticket_id")
        query = ticket.get("query")

        # Remove duplicate tickets
        if ticket_id in seen_ids:
            continue

        seen_ids.add(ticket_id)

        # Remove invalid queries
        if not query or not query.strip():
            continue

        # Remove HTML tags
        query = re.sub(r'<[^>]+>', '', query)

        # Remove unnecessary spaces
        query = query.strip()

        # Update ticket query
        ticket["query"] = query

        cleaned_tickets.append(ticket)

    return cleaned_tickets

def preprocess_text(text):

    # Define common English stop words
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

    # Tokenize text into individual words
    words = text.split()

    # Remove stop words
    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    return filtered_words