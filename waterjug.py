import heapq

class State:
    def __init__(self, jug_a, jug_b, parent=None, action=None, cost=0, heuristic=0):
        self.jug_a = jug_a
        self.jug_b = jug_b
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.jug_a == other.jug_a and self.jug_b == other.jug_b

def pour(jug_a, jug_b, capacity_a, capacity_b):
    # Pour from jug a to jug b
    if jug_a == 0:
        return 0, jug_b
    elif jug_b == capacity_b:
        return jug_a, jug_b
    else:
        space_available_b = capacity_b - jug_b
        poured = min(jug_a, space_available_b)
        return jug_a - poured, jug_b + poured

def get_successors(state, capacity_a, capacity_b):
    successors = []
    # Possible actions: (1) fill jug A, (2) fill jug B, (3) empty jug A, (4) empty jug B,
    # (5) pour from jug A to jug B, and (6) pour from jug B to jug A
    actions = [
        (capacity_a, state.jug_b),  # Fill jug A
        (state.jug_a, capacity_b),  # Fill jug B
        (0, state.jug_b),           # Empty jug A
        (state.jug_a, 0),           # Empty jug B
        pour(state.jug_a, state.jug_b, capacity_a, capacity_b),  # Pour from A to B
        pour(state.jug_b, state.jug_a, capacity_b, capacity_a)   # Pour from B to A
    ]
    for action in actions:
        successor = State(action[0], action[1])
        successors.append(successor)
    return successors

def heuristic(state, goal_amount):
    return abs(state.jug_a - goal_amount) + abs(state.jug_b - goal_amount)

def a_star(initial_state, capacity_a, capacity_b, goal_amount):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if (current_state.jug_a == goal_amount) or (current_state.jug_b == goal_amount):
            # Goal state found
            return current_state

        closed_set.add(current_state)

        for successor in get_successors(current_state, capacity_a, capacity_b):
            if successor not in closed_set:
                successor.cost = current_state.cost + 1
                successor.heuristic = heuristic(successor, goal_amount)
                successor.parent = current_state
                heapq.heappush(open_list, successor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        actions = []
        current_state = solution
        while current_state.parent:
            actions.append(current_state.action)
            current_state = current_state.parent
        actions.reverse()
        print("Solution:")
        for action in actions:
            print(action)

# Example usage
jug_capacity_a = 5
jug_capacity_b = 3
goal_amount = 4
initial_state = State(0, 0)
solution = a_star(initial_state, jug_capacity_a, jug_capacity_b, goal_amount)
print_solution(solution)
