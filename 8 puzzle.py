import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = 0
        if parent:
            self.cost = parent.cost + 1

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state.board[i][j]
            if value != 0:
                goal_row, goal_col = divmod(goal[value], 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def get_successors(state):
    successors = []
    zero_row, zero_col = None, None
    for i in range(3):
        for j in range(3):
            if state.board[i][j] == 0:
                zero_row, zero_col = i, j
                break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_board = [row[:] for row in state.board]
            new_board[zero_row][zero_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[zero_row][zero_col]
            successors.append(PuzzleState(new_board, state, (zero_row, zero_col)))
    return successors

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.move)
        state = state.parent
    return list(reversed(path))

def astar(initial_state, goal_state):
    open_list = []
    closed = set()
    heapq.heappush(open_list, initial_state)
    while open_list:
        current = heapq.heappop(open_list)
        if current == goal_state:
            return reconstruct_path(current)
        closed.add(current)
        for successor in get_successors(current):
            if successor not in closed:
                successor.cost = successor.cost + manhattan_distance(successor, goal_state.board)
                heapq.heappush(open_list, successor)
    return None

def main():
    initial_board = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]

    goal_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    initial_state = PuzzleState(initial_board)
    goal_state = PuzzleState(goal_board)

    path = astar(initial_state, goal_state)
    if path:
        print("Steps to reach the goal:")
        for step, move in enumerate(path):
            print(f"Step {step+1}: Move {initial_board[move[0]][move[1]]} to empty space")
    else:
        print("Goal state cannot be reached!")

if __name__ == "__main__":
    main()
