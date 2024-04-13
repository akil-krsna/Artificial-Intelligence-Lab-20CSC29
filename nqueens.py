import random
import math

def generate_initial_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

def heuristic(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def generate_successor(state):
    n = len(state)
    current_conflicts = heuristic(state)
    best_state = state
    for i in range(n):
        for j in range(n):
            if state[i] != j:
                new_state = state[:]
                new_state[i] = j
                new_conflicts = heuristic(new_state)
                if new_conflicts < current_conflicts:
                    best_state = new_state
                    current_conflicts = new_conflicts
    return best_state

def a_star(n, max_iterations=1000):
    current_state = generate_initial_state(n)
    for _ in range(max_iterations):
        if heuristic(current_state) == 0:
            return current_state
        current_state = generate_successor(current_state)
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        for row in solution:
            print(" ".join("Q" if i == row else "_" for i in range(len(solution))))

# Example usage
n = 8  # Number of queens
solution = a_star(n)
print_solution(solution)
