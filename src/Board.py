class Board:
    def __init__(self):
        self.board = self.initialize_board()
        self.move_history = []

    def __init__(self):
        # Initial board setup with pieces positioned
        return [
            [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK],
            [PAWN] * 8,
            [EMPTY] * 8,
            [EMPTY] * 8,
            [EMPTY] * 8,
            [EMPTY] * 8,
            [PAWN] * 8,
            [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        ]

    def print_board(self):
        # Print the board in a user-friendly way
        for row in self.board:
            print(' '.join(row))
        print()

    def is_square_occupied(self, row, col):
        # Check if a square is occupied by a piece
        return self.board[row][col] != EMPTY

    def get_piece(self, row, col):
        # Get the piece at the given position
        return self.board[row][col]

    def set_piece(self, row, col, piece):
        # Place a piece at the given position
        self.board[row][col] = piece

    def move_piece(self, move):
        # Execute a move on the board
        from_row, from_col = move.from_square
        to_row, to_col = move.to_square
        piece = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, piece)
        self.set_piece(from_row, from_col, EMPTY)
        self.move_history.append(move)

    def undo_move(self):
        # Undo the last move made
        if self.move_history:
            last_move = self.move_history.pop()
            from_row, from_col = last_move.to_square
            to_row, to_col = last_move.from_square
            piece = self.get_piece(from_row, from_col)
            self.set_piece(to_row, to_col, piece)
            self.set_piece(from_row, from_col, EMPTY)

    def get_legal_moves(self, player):
        # Generate all legal moves for the given player
        legal_moves = []
        # Logic to generate moves goes here
        return legal_moves

