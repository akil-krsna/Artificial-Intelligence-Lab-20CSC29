import heapq

class State:
    def __init__(self, jug1, jug2, parent=None):
        self.jug1 = jug1
        self.jug2 = jug2
        self.parent = parent
        self.cost = 0
        if parent:
            self.cost = parent.cost + 1

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def is_goal(state, target):
    return state.jug1 == target or state.jug2 == target

def get_successors(state, capacity1, capacity2):
    successors = []
    # fill jug1
    successors.append(State(capacity1, state.jug2, state) if state.jug1 != capacity1 else None)
    # fill jug2
    successors.append(State(state.jug1, capacity2, state) if state.jug2 != capacity2 else None)
    # empty jug1
    successors.append(State(0, state.jug2, state) if state.jug1 != 0 else None)
    # empty jug2
    successors.append(State(state.jug1, 0, state) if state.jug2 != 0 else None)
    # pour jug1 to jug2
    pour_amount = min(state.jug1, capacity2 - state.jug2)
    successors.append(State(state.jug1 - pour_amount, state.jug2 + pour_amount, state) if pour_amount != 0 else None)
    # pour jug2 to jug1
    pour_amount = min(state.jug2, capacity1 - state.jug1)
    successors.append(State(state.jug1 + pour_amount, state.jug2 - pour_amount, state) if pour_amount != 0 else None)
    return [succ for succ in successors if succ is not None]

def heuristic(state, target):
    return abs(state.jug1 - target) + abs(state.jug2 - target)

def astar(initial, target, capacity1, capacity2):
    open_list = []
    closed = set()
    heapq.heappush(open_list, initial)
    while open_list:
        current = heapq.heappop(open_list)
        if is_goal(current, target):
            path = []
            while current:
                path.append((current.jug1, current.jug2))
                current = current.parent
            return list(reversed(path))
        closed.add(current)
        for successor in get_successors(current, capacity1, capacity2):
            if successor not in closed:
                successor.cost = successor.cost + heuristic(successor, target)
                heapq.heappush(open_list, successor)
    return None

def main():
    capacity1 = int(input("Enter capacity of jug 1: "))
    capacity2 = int(input("Enter capacity of jug 2: "))
    target = int(input("Enter target amount of water: "))
    initial_state = State(0, 0)
    path = astar(initial_state, target, capacity1, capacity2)
    if path:
        print("Steps to reach target:")
        for step, (jug1, jug2) in enumerate(path):
            print(f"Step {step+1}: Jug 1 = {jug1}, Jug 2 = {jug2}")
    else:
        print("Target cannot be reached!")

if __name__ == "__main__":
    main()
