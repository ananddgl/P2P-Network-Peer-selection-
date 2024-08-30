import numpy as np

def generate_random_constraints(num_constraints, num_variables, seed=None):
    """
    Generates random coefficients for inequality constraints in a linear programming problem.
    
    Parameters:
        num_constraints (int): Number of inequality constraints.
        num_variables (int): Number of variables in the linear programming problem.
        seed (int, optional): Random seed for reproducibility.
        
    Returns:
        A (ndarray): Coefficients for the inequality constraints.
        b (ndarray): Right-hand side values for the inequality constraints.
    """
    if seed is not None:
        np.random.seed(seed)
    
    A = np.random.randint(1, 10, size=(num_constraints, num_variables))
    b = np.random.randint(1, 20, size=num_constraints)
    
    return A, b

def generate_random_objective_function(num_variables, seed=None):
    """
    Generates random coefficients for the objective function in a linear programming problem.
    
    Parameters:
        num_variables (int): Number of variables in the linear programming problem.
        seed (int, optional): Random seed for reproducibility.
        
    Returns:
        c (ndarray): Coefficients for the objective function.
    """
    if seed is not None:
        np.random.seed(seed)
    
    c = np.random.randint(1, 10, size=num_variables)
    
    return c

if __name__ == "__main__":
    # Example usage
    num_constraints = 3
    num_variables = 3
    A, b = generate_random_constraints(num_constraints, num_variables, seed=42)
    c = generate_random_objective_function(num_variables, seed=42)
    
    print("Generated A:", A)
    print("Generated b:", b)
    print("Generated c:", c)
