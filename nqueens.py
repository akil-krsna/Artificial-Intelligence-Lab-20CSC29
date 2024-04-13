def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, n, result):
    if row == n:
        result.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, result)
            board[row][col] = 0

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    result = []
    solve_nqueens_util(board, 0, n, result)
    return result

def print_solution(board):
    for row in board:
        print(' '.join('Q' if cell else '.' for cell in row))

def main():
    n = 8  # Change n to the desired board size
    solutions = solve_nqueens(n)
    print(f"Total solutions for {n}-queens problem:", len(solutions))
    for i, solution in enumerate(solutions, start=1):
        print(f"\nSolution {i}:")
        print_solution(solution)

if __name__ == "__main__":
    main()
