def is_safe(x, y, board, n):
    """Sprawdza, czy pole (x, y) jest bezpieczne do odwiedzenia."""
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def rozwiaz_problem_skoczka(n):
    """Rozwiązuje problem skoczka szachowego dla szachownicy nxn z dowolnego punktu startowego."""
    # Możliwe ruchy skoczka (x, y)
    knight_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    for start_x in range(n):
        for start_y in range(n):
            # Inicjalizacja szachownicy dla każdego punktu startowego
            board = [[-1 for _ in range(n)] for _ in range(n)]
            board[start_x][start_y] = 0
            print(f"Rozpoczynając od punktu ({start_x}, {start_y}):")
            droga_skoczka(start_x, start_y, 1, board, knight_moves, n)

def droga_skoczka(x, y, move_count, board, knight_moves, n):
    """Rekurencyjna funkcja rozwiązująca problem za pomocą backtracking."""
    if move_count == n * n:
        # Wyświetl bieżące rozwiązanie
        print("Znaleziono rozwiązanie:")
        print_board(board)
        print()
        return

    for move in knight_moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_safe(next_x, next_y, board, n):
            board[next_x][next_y] = move_count
            droga_skoczka(next_x, next_y, move_count + 1, board, knight_moves, n)
            # Cofnij ruch (backtracking)
            board[next_x][next_y] = -1

def print_board(board):
    """Wyświetla szachownicę z trasą skoczka."""
    for row in board:
        print(' '.join(f'{cell:2}' for cell in row))

n =  5
rozwiaz_problem_skoczka(n)
