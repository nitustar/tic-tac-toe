import exceptions.InvalidGameConstructionParametersException
import strategies.gamewinningstrategy.GameWinningStrategy
import strategies.gamewinningstrategy.OrderOneGameWinningStrategy
from models.Board import Board
from models.GameStatus import GameStatus
from models.Move import Move


class Builder:
    pass


class Game:
    def __init__(self):
        self.__board = None
        self.__players = None
        self.__moves = []
        self.__gameStatus = None
        self.__nextPlayerIndex = None
        self.__gameWinningStrategy = None
        self.__winner = None

    def get_winner(self):
        return self.__winner

    def set_winner(self, winner):
        self.__winner = winner

    def get_game_winning_strategy(self):
        return self.__gameWinningStrategy

    def set_game_winning_strategy(self, game_winning_strategy):
        self.__gameWinningStrategy = game_winning_strategy

    @staticmethod
    def get_builder():
        return Builder()

    def undo(self):
        pass

    def makeNextMove(self):
        toMovePlayer = self.__players[self.__nextPlayerIndex]

        print("It is " + self.__players[self.__nextPlayerIndex].getName() + "'s turn.")

        move = toMovePlayer.decideMove(self.__board)

        # validate move
        row = move.getCell().getRow()
        col = move.getCell().getCol()

        print("Move happened at: " + str(row) + ", " + str(col) + ".")

        self.__board.getBoard()[row][col].setCellState(CellState.FILLED)
        self.__board.getBoard()[row][col].setPlayer(self.__players[self.__nextPlayerIndex])

        finalMove = Move(
            self.__players[self.__nextPlayerIndex],
            self.__board.getBoard()[row][col]
        )

        self.__moves.append(finalMove)

        if self.__gameWinningStrategy.checkWinner(
                self.__board, self.__players[self.__nextPlayerIndex], finalMove.getCell()
        ):
            self.__gameStatus = GameStatus.ENDED
            self.__winner = self.__players[self.__nextPlayerIndex]

        self.__nextPlayerIndex += 1
        self.__nextPlayerIndex %= len(self.__players)

    def displayBoard(self):
        self.__board.display()

    def get_board(self):
        return self.__board

    def set_board(self, board):
        self.__board = board

    def get_players(self):
        return self.__players

    def set_players(self, players):
        self.__players = players

    def get_moves(self):
        return self.__moves

    def set_moves(self, moves):
        self.__moves = moves

    def get_game_status(self):
        return self.__gameStatus

    def set_game_status(self, game_status):
        self.__gameStatus = game_status

    def get_next_player_index(self):
        return self.__nextPlayerIndex

    def set_next_player_index(self, next_player_index):
        self.__nextPlayerIndex = next_player_index

    class Builder:
        def __init__(self):
            self.dimension = None
            self.__players = None

        def set_dimension(self, dimension):
            self.dimension = dimension
            return self

        def set_players(self, players):
            self.__players = players
            return self

        def valid(self):
            if self.dimension < 3:
                raise InvalidGameConstructionParametersException("Dimension of game can't be 1")

            if len(self.__players) != self.dimension - 1:
                raise InvalidGameConstructionParametersException("Number of Players must be Dimension - 1")

            # Validate no 2 people with same char

            # Validate all 1 bot

            return True

        def build(self):
            try:
                self.valid()
            except Exception as e:
                raise InvalidGameConstructionParametersException(e.args[0])

            game = Game()
            game.set_game_status(GameStatus.IN_PROGRESS)
            game.set_players(self.__players)
            game.set_moves([])
            game.set_board(Board(self.dimension))
            game.set_next_player_index(0)

