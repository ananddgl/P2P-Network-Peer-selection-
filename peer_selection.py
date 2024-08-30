import numpy as np
from scipy.optimize import linprog
from scipy.optimize import OptimizeResult

def fuzzy_linear_programming(c, A, b, bounds=None, options=None):
    """
    Solves a fuzzy linear programming problem using SciPy's linprog function.
    
    Parameters:
        c (array_like): Coefficients of the linear objective function to be minimized.
        A (array_like): 2-D array which, when matrix-multiplied by x, gives the values of the inequality constraints at x.
        b (array_like): 1-D array of values representing the upper-bound of each inequality constraint (row) in A_ub.
        bounds (sequence of tuples): Bounds for variables, as a sequence of (min, max) pairs for each element in x.
        options (dict): A dictionary of solver options.
        
    Returns:
        result (OptimizeResult): The optimization result represented as a `scipy.optimize.OptimizeResult` object.
    """
    # Solve the linear programming problem
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs', options=options)
    
    return result

def main():
    # Coefficients of the objective function
    c = np.array([1, 2, 3])
    
    # Coefficients of the inequality constraints
    A = np.array([[1, 1, 0], [0, 2, 1], [1, 0, 2]])
    
    # Right-hand side of the inequality constraints
    b = np.array([4, 6, 8])
    
    # Bounds on the variables
    bounds = [(0, None), (0, None), (0, None)]
    
    # Solve the fuzzy linear programming problem
    result = fuzzy_linear_programming(c, A, b, bounds)
    
    # Display the result
    if result.success:
        print("Optimal solution found:", result.x)
    else:
        print("No optimal solution found. Status:", result.status)

if __name__ == "__main__":
    main()
