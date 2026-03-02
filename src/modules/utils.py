import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.cards import *
from src.card_index import *
from src.modules.parser import *
import copy
from typing import Dict, Any


def update_card(card: Card, game_state: Dict[str, Any], player: str) -> CreatureCard:
    """
    Updates the card after executing the effect. Works only for Creature cards.

    :param card: The card to update.
    :type card: Card
    :param game_state
    """

    if not isinstance(card, CreatureCard):
        return card     # Not a creature

    updated_card = copy.deepcopy(card)
    instructions = Parser(card.effect).parse()

    for ins in instructions:
        if ins.get("trigger"):
            continue

        action = ins.get("action")
        
        
        field = ins.get("field")
        value = ins.get("value")
        if type(value) == tuple:
            value = resolve_expr(value, game_state, player)

        if action == "inc":
            if field == "att":
                updated_card.attack += value
            elif field == "end":
                updated_card.defence += value

        elif action == "dec":
            if field == "att":
                update_card.attack -= value
            elif field == "end":
                updated_card.defence -= value

    return updated_card

def resolve_expr(expr: str, game_state: Dict[str, Any], player: str) -> int:
    """
    Resolves a tuple expression.

    :param expr: The expression to resolve.
    :type expr: str
    :param game_state: The game state dictionary
    :type game_state: Dict[str, Any]
    :param player: The player's move.
    :type player: str
    """
    if type(expr) != tuple or len(expr) == 0:
        return 0
    
    if len(expr) >= 3 and expr[1] == "count":
        place = expr[0]
        subject = expr[2]
        if type(subj) == str:
            subject = subject.strip('"').strip("'")

        player_data = game_state[player]

        if place == "mana":
            colour = subject.lower()
            return player_data.get(f"{colour}_mana", 0)

        if place in ["graveyard", "deck", "hand"]:
            cards = player_data.get(place, [])
            count = 0
            for card in cards:
                if type(card) == dict and card.get("name") == subject:
                    count += 1
                elif hasattr(card, "name") and card.name == "subject":
                    count += 1

            return count

    return 0

