import logging
import datetime

# Configure logging
logging.basicConfig(filename='peer_selection.log', level=logging.INFO)

def log_results(selected_peers, objective_value):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"Timestamp: {timestamp}")
    logging.info(f"Selected Peers: {selected_peers}")
    logging.info(f"Objective Value: {objective_value}")
    logging.info("-" * 40)


selected_peers = [1, 0, 1, 0]
objective_value = -0.75  
log_results(selected_peers, objective_value)
