import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_fallback_data():

    logging.warning("Using fallback mock documents.")

    return [
        {
            "doc_id": 101,
            "title": "Introduction to Python",
            "content": "Python is a popular programming language.",
            "word_count": 7
        },
        {
            "doc_id": 102,
            "title": "Introduction to AI",
            "content": "Artificial intelligence enables machines to perform intelligent tasks.",
            "word_count": 8
        }
    ]

def fetch_posts():

    url = "https://jsonplaceholder.typicode.com/posts"

    logging.info("Starting API request...")

    try:

        # Send GET request
        response = requests.get(url, timeout=10)

        # Check HTTP response
        response.raise_for_status()

        # Convert response into JSON
        posts = response.json()

        # Extract first 5 posts
        posts = posts[:5]

        documents = []

        for post in posts:

            document = {
                "doc_id": post["id"],
                "title": post["title"].strip(),
                "content": post["body"].replace("\n", " ").strip(),
                "word_count": len(post["body"].split())
            }

            documents.append(document)

        logging.info("API request successful!")
        logging.info("Fetched %d documents", len(documents))

        return documents

    except requests.exceptions.Timeout:
        logging.error("API request timed out!")

    except requests.exceptions.ConnectionError:
        logging.error("Unable to connect to API!")

    except requests.exceptions.HTTPError as error:
        logging.error("HTTP error occurred: %s", error)

    except requests.exceptions.RequestException as error:
        logging.error("Request failed: %s", error)

    return get_fallback_data()


# Main program
if __name__ == "__main__":

    documents = fetch_posts()

    print("\nFetched Documents:")

    for document in documents:
        print(document)