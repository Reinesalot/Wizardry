import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.card_index import *


class GameEngine:
    def __init__(self, game_key: str, p1: str, p2: str) -> None:
        """
        The game engine for Wizardry. Manages the JSON files.

        :param game_key: The game's specific ID key.
        :type game_key: str
        :param p1: Player 
        """
        self.game_key = game_key
        self.p1 = p1
        self.p2 = p2

