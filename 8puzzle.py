import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.state == other.state

class PuzzleState:
    def __init__(self, board):
        self.board = board

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

def get_successors(state):
    successors = []
    zero_index = state.board.index(0)
    rows, cols = 3, 3

    # Possible moves: left, right, up, down
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for move in moves:
        new_row = zero_index // cols + move[0]
        new_col = zero_index % cols + move[1]

        if 0 <= new_row < rows and 0 <= new_col < cols:
            new_board = state.board[:]
            new_zero_index = new_row * cols + new_col
            new_board[zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero_index]
            successor = PuzzleNode(PuzzleState(new_board))
            successors.append(successor)

    return successors

def heuristic(state, goal_state):
    return sum(1 for i in range(len(state.board)) if state.board[i] != goal_state.board[i])

def a_star(initial_state, goal_state):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, initial_state)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            # Goal state found
            return current_node

        closed_set.add(current_node)

        for successor in get_successors(current_node.state):
            if successor not in closed_set:
                successor.cost = current_node.cost + 1
                successor.heuristic = heuristic(successor.state, goal_state)
                successor.parent = current_node
                heapq.heappush(open_list, successor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        actions = []
        current_node = solution
        while current_node.parent:
            actions.append(current_node.action)
            current_node = current_node.parent
        actions.reverse()
        print("Solution:")
        for action in actions:
            print(action)

# Example usage
initial_state = PuzzleNode(PuzzleState([1, 2, 3, 4, 5, 6, 7, 0, 8]))
goal_state = PuzzleState([1, 2, 3, 4, 5, 6, 7, 8, 0])
solution = a_star(initial_state, goal_state)
print_solution(solution)
