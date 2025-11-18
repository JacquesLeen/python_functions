"""A simple Wikipedia bot to fetch summaries of topics."""

import wikipedia
import click


@click.command()
@click.option("--sentences", default=2, help="Number fo sentences for the summary.")
@click.option("--name", prompt="Wikipedia Page", help="Page that you want to scrape")
def get_wikipedia_summary(name, sentences):
    """
    Fetches a summary of a given topic from Wikipedia.

    Parameters:
    name (str): The topic to search for on Wikipedia.
    sentences (int): The number of sentences to include in the summary.

    Returns:
    str: A summary of the topic from Wikipedia.
    """
    try:
        summary = wikipedia.summary(name, sentences=sentences)
        click.echo(click.style(f"{summary}", fg="green", bg="black"))
    except wikipedia.exceptions.DisambiguationError as e:
        click.echo(click.style(f"Disambiguation error: {e.options}", fg="yellow", bg="black"))
    except wikipedia.exceptions.PageError:
        click.echo(click.style(f"Page not found: {e.options}", fg="red", bg="black"))
    except Exception as e:
        click.echo(click.style(f"An error occurred: {str(e)}", fg="red", bg="black"))




