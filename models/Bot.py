import factories.BotPlayingStrategyFactory
import strategies.botplayingstrategy
class Bot(Player):
    def __init__(self, name, aSymbol, difficultyLevel):
        super().__init__(name, aSymbol, PlayerType.BOT)
        self.botDifficultyLevel = difficultyLevel
        self.botPlayingStrategy = BotPlayingStrategyFactory.getStrategyForDifficultyLevel(difficultyLevel)

    def get_BotDifficultyLevel(self):
        return self.botDifficultyLevel

    def set_BotDifficultyLevel(self, botDifficultyLevel):
        self.botDifficultyLevel = botDifficultyLevel

    def decideMove(self, board):
        return self.botPlayingStrategy.decideMove(self, board)