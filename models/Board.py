
class Board:
    def __init__(self, dimension):
        self.__board = []

        for i in range(dimension):
            self.__board.append([])
            for j in range(dimension):
                self.__board[i].append(Cell(i, j))

    def display(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                if self.__board[i][j].getCellState() == CellState.EMPTY:
                    print("|   |", end="")
                else:
                    print("| " + self.__board[i][j].getPlayer().getSymbol() + " |", end="")
            print("\n")

    def get_board(self):
        return self.__board

    def set_board(self, board):
        self.__board = board

