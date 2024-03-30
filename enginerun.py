from engine.engine import Game
from engine.config import NUM_GAMES, NUM_ROUNDS

for _ in range(NUM_GAMES):
    Game().run_match()
