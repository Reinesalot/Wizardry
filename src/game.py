import sys
import os
from pathlib import Path
import copy

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.card_index import *
from src.modules.utils import *


# TODO: Game setup
# TODO: Core game loop (playing cards, blocking, etc.)

class GameEngine:
    def __init__(self, game_key: str, p1: str, p2: str, p1_deck: list[Card], p2_deck: list[Card]) -> None:
        """
        The game engine for Wizardry. Manages the JSON files.

        :param game_key: The game's specific ID key.
        :type game_key: str
        :param p1: Player 
        """
        
        # Setup and define variables
        self.game_key = game_key
        self.p1 = p1
        self.p2 = p2

        self.state_path = Path(__file__).resolve().parent.parent / f"db//{game_key}//game_state.json"
        self.priority_player = self.p1
        
        # Setup game state
        
        data = { p1:
                    {
                        "deck": [],
                        "hand": [],
                        "battlefield": [],
                        "lands": [],
                        "graveyard": [],
                        "blue_mana": 0,
                        "red_mana": 0,
                        "green_mana": 0
                    }
                }
        i = 0

        for card in p1_deck:
            card.id = i
            data[p1]["deck"].append(
                { str(card.id):
                    {
                        "name": card.name,
                        "generic_mana": card.generic_mana,
                        "sp_mana": card.sp_mana,
                        "description": card.description,
                        "tapped": card.tapped,
                        "statuses": card.statuses,
                        "effect": card.effect,
                    }
                }
            )

