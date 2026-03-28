from src.game import *
from src.cards import *
from src.card_index import *


game = GameEngine().start_game(game_key="test", p1="player1", p2="player2", p1_deck=[skeleton, skeleton, vergil, forest], p2_deck=[berserker, skeleton, vergil, forest])
print(game.get_state("test"))