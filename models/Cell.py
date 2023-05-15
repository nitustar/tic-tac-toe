class Cell:
    def __init__(self, row, col):
        self.__player = None
        self.__row = row
        self.__col = col
        self.__cellState = 'EMPTY'

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player

    def get_row(self):
        return self.__row

    def set_row(self, row):
        self.__row = row

    def get_col(self):
        return self.__col

    def set_col(self, col):
        self.__col = col

    def get_cell_state(self):
        return self.__cellState
q
    def set_cell_state(self, cell_state):
        self.__cellState = cell_state
