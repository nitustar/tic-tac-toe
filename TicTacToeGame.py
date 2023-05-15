from typing import List
from tic_tac_toe import GameController, Game, Player, Bot, PlayerType, BotDifficultyLevel, GameStatus

if __name__ == '__main__':
    # It will take input: dimension, players
    game_controller = GameController()

    print("What should be the dimension of game?")
    dimension = int(input())

    print("Will there be any bot? y/n")
    is_bot_string = input()

    players = []

    to_iterate = dimension - 1

    if is_bot_string == "y":
        to_iterate = dimension - 2

    for i in range(to_iterate):
        print("What is the name of player " + str(i))
        player_name = input()

        print("What is the char of player " + str(i))
        player_symbol = input()

        players.append(Player(player_name, player_symbol[0], PlayerType.HUMAN))

    if is_bot_string == "y":
        print("What is the name of bot?")
        player_name = input()

        print("What is the char of bot?")
        player_symbol = input()

        players.append(Bot(player_name, player_symbol[0], BotDifficultyLevel.EASY))

    game = game_controller.create_game(dimension, players)

    while game_controller.get_game_status(game) == GameStatus.IN_PROGRESS:
        print("This is the current board:")
        game_controller.display_board(game)

        print("Does anyone want to undo? y/n")
        input_str = input()

        if input_str == "y":
            game_controller.undo(game)
        else:
            game_controller.execute_next_move(game)

    print("Game has ended. Result was: ")
    if game.get_game_status() != GameStatus.DRAW:
        print("Winner is: ." + game_controller.get_winner(game).get_name())
