"""A simple Wikipedia bot to fetch summaries of topics."""

import wikipedia

def get_wikipedia_summary(topic, sentences=2):
    """
    Fetches a summary of a given topic from Wikipedia.

    Parameters:
    topic (str): The topic to search for on Wikipedia.
    sentences (int): The number of sentences to include in the summary.

    Returns:
    str: A summary of the topic from Wikipedia.
    """
    try:
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
