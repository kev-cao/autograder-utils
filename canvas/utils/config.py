import json

def load_config(folder):
    """
    Loads the configuration file for the Canvas API and returns it.

    Params:
    folder (String) : The folder containing the config.

    Returns:
    json : The config file as a JSON object.
    """
    try:
        with open(f'{folder}/config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Make sure to run setup.py before running the scraper.")
