import pandas as pd
import requests
from app.services.plot_generator import generate_scatter_plot

async def process(qtext, files):
    df = pd.read_html("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")[0]
    # Clean and process data
    # Calculate answers
    # Generate plot
    return [q1, q2, q3, base64plot]
