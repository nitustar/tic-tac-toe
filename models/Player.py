class Player:
    def __init__(self, name, symbol, player_type):
        self.name = name
        self.symbol = symbol
        self.type = player_type

    def decide_move(self, board):
        print("Please tell the row, starting from :")
        row = int(input())

        print("Please tell the col, starting from 0:")
        col = int(input())

        return Move(self, Cell(row, col))

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, player_type):
        self.type = player_type
