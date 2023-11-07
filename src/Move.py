class Move:
    def __init__(self, from_square, to_square):
        self.from_square = from_square
        self.to_square = to_square

    def __repr__(self):
        return f"{self.from_square}->{self.to_square}"