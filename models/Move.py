
class Move:
    def __init__(self, player, cell):
        self.player = player
        self.cell = cell

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    def get_cell(self):
        return self.cell

    def set_cell(self, cell):
        self.cell = cell
