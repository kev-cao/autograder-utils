import json

def load_config():
    """
    Loads the configuration file for the Canvas API and returns it.

    Returns:
    json : The config file as a JSON object.
    """
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Make sure to run setup.py before running the scraper.")
