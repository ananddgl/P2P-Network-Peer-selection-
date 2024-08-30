import json

def load_config(filepath):
    """
    Load configuration settings from a JSON file.
    """
    with open(filepath, 'r') as file:
        config = json.load(file)
    return config

if __name__ == "__main__":
    config = load_config('config.json')
    print(config)
