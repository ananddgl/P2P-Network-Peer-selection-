import pandas as pd

def load_peer_data(filepath):
    """
    Load peer data from a CSV file.
    """
    data = pd.read_csv(filepath)
    return data

def preprocess_data(data):
    """
    Preprocess data (e.g., normalize, handle missing values).
    """
    # Example: Normalize Cost, Latency, and Performance
    data['Cost'] = (data['Cost'] - data['Cost'].min()) / (data['Cost'].max() - data['Cost'].min())
    data['Latency'] = (data['Latency'] - data['Latency'].min()) / (data['Latency'].max() - data['Latency'].min())
    data['Performance'] = (data['Performance'] - data['Performance'].min()) / (data['Performance'].max() - data['Performance'].min())
    return data

if __name__ == "__main__":
    data = load_peer_data('peers_data.csv')
    processed_data = preprocess_data(data)
    processed_data.to_csv('processed_peers_data.csv', index=False)
