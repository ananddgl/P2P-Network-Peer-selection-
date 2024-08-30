import logging

def log_results(results):
    """
    Log the results of the simulation.
    """
    logging.basicConfig(filename='simulation.log', level=logging.INFO)
    for i, (selected_peers, objective_value) in enumerate(results):
        logging.info(f"Simulation {i+1}: Selected Peers: {selected_peers}, Objective Value: {objective_value}")

if __name__ == "__main__":
    import pickle
    
    with open('simulation_results.pkl', 'rb') as f:
        results = pickle.load(f)
    
    log_results(results)
    print("Results logged.")
