"""A simple Wikipedia bot to fetch summaries of topics."""

import wikipedia
import click


def fetch_wikipedia_summary(name, sentences=2):
    """
    Fetches a summary of a given topic from Wikipedia.

    Parameters:
    name (str): The topic to search for on Wikipedia.
    sentences (int): The number of sentences to include in the summary.

    Returns:
    str: A summary of the topic from Wikipedia.

    Raises:
    wikipedia.exceptions.DisambiguationError: If the topic is ambiguous.
    wikipedia.exceptions.PageError: If the page is not found.
    """
    summary = wikipedia.summary(name, sentences=sentences)
    return summary


@click.command()
@click.option("--sentences", default=2, help="Number of sentences for the summary.")
@click.option("--name", required=True, help="Page that you want to scrape")
def get_wikipedia_summary(name, sentences=2):
    """
    CLI command to fetch a summary of a given topic from Wikipedia.
    """
    try:
        summary = fetch_wikipedia_summary(name, sentences=sentences)
        click.echo(click.style(f"{summary}", fg="green", bg="black"))
    except wikipedia.exceptions.DisambiguationError as e:
        click.echo(
            click.style(f"Disambiguation error: {e.options}", fg="yellow", bg="black")
        )
    except wikipedia.exceptions.PageError:
        click.echo(click.style(f"Page not found", fg="red", bg="black"))
    except Exception as e:
        click.echo(click.style(f"An error occurred: {str(e)}", fg="red", bg="black"))
