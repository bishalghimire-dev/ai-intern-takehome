# AI Intern Take-Home Assignment

## Project Overview

This project is developed as part of the AI Intern pre-hiring technical assignment.

It demonstrates Python programming, basic Natural Language Processing (NLP), REST API integration, error handling, prompt engineering, Retrieval-Augmented Generation (RAG), and AI safety concepts.

## Technologies Used

- Python 3.11
- Requests
- Regular Expressions (Regex)
- JSON
- Collections (Counter)
- Logging
- Git and GitHub

## Project Structure

```text
ai-intern-takehome/
│
├── data/
│   ├── support_tickets.json
│   └── cleaned_tickets.json
│
├── task1_nlp_cleaner.py
├── task2_api_client.py
├── ANSWERS.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/bishalghimire-dev/ai-intern-takehome.git
cd ai-intern-takehome
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Part 1: Python Data Cleaning and NLP

File: `task1_nlp_cleaner.py`

This script performs the following operations:

- Removes duplicate tickets based on ticket ID.
- Filters invalid and empty queries.
- Removes HTML tags and unnecessary whitespace.
- Converts text into lowercase.
- Removes punctuation and special characters.
- Tokenizes text into individual words.
- Removes common English stop words.
- Calculates ticket counts by category.
- Identifies the top five frequent keywords.
- Saves cleaned and tokenized records into `data/cleaned_tickets.json`.

### Run the script

```bash
python task1_nlp_cleaner.py
```

## Part 2: Public API Integration

File: `task2_api_client.py`

This script connects to the JSONPlaceholder public REST API.

Endpoint:

https://jsonplaceholder.typicode.com/posts

Features:

- Sends HTTP GET requests.
- Uses a 10-second timeout.
- Retrieves the first five posts.
- Extracts document ID, title, content, and word count.
- Handles network errors and HTTP errors.
- Uses Python logging to monitor API requests.
- Provides two fallback mock documents if the API request fails.

### Run the script

```bash
python task2_api_client.py
```

## Part 3: AI, RAG and Safety Concepts

Written answers are available in `ANSWERS.md`.

Topics covered:

- Prompt engineering and hallucination prevention.
- Temperature and Top_p.
- RAG document chunking and chunk overlap.
- Prompt injection attacks.
- AI safety and defensive guardrails.

## Assumptions and Challenges

### Assumptions

- The first occurrence of a duplicate ticket ID is retained.
- Tickets with null, empty, or whitespace-only queries are considered invalid.
- A predefined set of common English stop words is used.
- The API returns posts in the expected JSON format.
- If the API request fails, two predefined mock documents are returned.

### Challenges Encountered

- Handling duplicate and invalid JSON records.
- Removing HTML tags and punctuation using regular expressions.
- Implementing keyword frequency analysis.
- Handling API connection failures and timeouts.
- Understanding RAG chunking and prompt injection prevention.

## Author

**Bishal Ghimire**

AI Intern Technical Assignment