from collections import deque
# Function to pour water from one jug to another
def pour(state, jug1, jug2):
    amt = min(state[jug1], (jug_caps[jug2] - state[jug2]))
    new_state = list(state)
    new_state[jug1] -= amt
    new_state[jug2] += amt
    return tuple(new_state)
# Function to generate successor states
def get_successors(state):
    successors = []
    # Pouring operations between jugs
    for jug1, jug2 in [(0, 1), (1, 0)]:
        new_state = pour(state, jug1, jug2)
        if new_state != state:
            successors.append(new_state)
    # Fill operations for each jug
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = jug_caps[jug]
        successors.append(tuple(new_state))
    # Empty operations for each jug
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = 0
        successors.append(tuple(new_state))
    return successors
# Heuristic function for A* algorithm
def heuristic(state, goal):
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))
# A* search algorithm
def a_star(start, goal):
    open_list = [(heuristic(start, goal), start)]
    closed_list = set()
    parent = {start: None}
    while open_list:
        _, curr_state = open_list.pop(0)
        if curr_state == goal:
            # Reconstructing the path
            path = deque()
            state = curr_state
            while state is not None:
                path.appendleft(state)
                state = parent[state]
            return list(path)
        closed_list.add(curr_state)
        for succ_state in get_successors(curr_state):
            if succ_state not in closed_list:
                succ_cost = heuristic(succ_state, goal)
                open_list.append((succ_cost, succ_state))
                open_list.sort()  # Sorting based on heuristic cost
                parent[succ_state] = curr_state
    return None
# Jug capacities and initial/final states
jug_caps = (4, 3)
start_state = (0, 0)
goal_state = (2, 0)
# Running A* algorithm and printing solution
solution = a_star(start_state, goal_state)
if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution exists.")