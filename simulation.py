import numpy as np
import pandas as pd
from scipy.optimize import linprog
import matplotlib.pyplot as plt
import json
import logging
import datetime

# Load peer data from CSV
data = pd.read_csv('peers_data.csv')

# Load config settings
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Configure logging
logging.basicConfig(filename='simulation.log', level=logging.INFO)

# Define fuzzy membership functions
def membership(x, min_val, max_val):
    return (x - min_val) / (max_val - min_val)

# Run simulation
num_simulations = 100
results = []

for i in range(num_simulations):
    # Vary peer data for each simulation
    data['Cost'] = np.random.uniform(0.5, 1.0, len(data))
    data['Latency'] = np.random.uniform(0.1, 0.4, len(data))
    data['Performance'] = np.random.uniform(0.7, 1.0, len(data))

    # Apply membership function to coefficients to handle fuzziness
    c = data['Cost'].values
    c_fuzzy = np.array([membership(ci, min(c), max(c)) for ci in c])

    # Constraints matrix (A) and bounds (b)
    A = np.array([
        [1, 1, 0, 0],  # Constraint 1
        [0, 0, 1, 1],  # Constraint 2
        [1, 0, 1, 0],  # Constraint 3
        [0, 1, 0, 1]   # Constraint 4
    ])
    b = np.array([1, 1, 1, 1])  # Example upper bounds for the constraints

    # Bounds for each peer (e.g., binary decision 0 or 1)
    x_bounds = [(0, 1) for _ in range(len(c))]

    # Solving the fuzzy linear programming problem
    res = linprog(c_fuzzy, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

    if res.success:
        selected_peers = res.x
        objective_value = res.fun
        results.append((selected_peers, objective_value))
        
        # Log results
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Simulation {i+1} - Timestamp: {timestamp}")
        logging.info(f"Selected Peers: {selected_peers}")
        logging.info(f"Objective Value: {objective_value}")
        logging.info("-" * 40)

# Analyze and visualize results
objectives = [result[1] for result in results]
plt.figure(figsize=(10, 6))
plt.plot(objectives, marker='o', linestyle='-', color='b', label='Objective Value')
plt.xlabel('Simulation Run')
plt.ylabel('Objective Value')
plt.title('Objective Values over Multiple Simulation Runs')
plt.legend()
plt.show()
