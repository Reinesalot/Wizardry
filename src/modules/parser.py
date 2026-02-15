"""
Docstring for modules.parser

A parser to parse card effects. The syntax is as follows:

- Trigger? -> Action -> Field/Static -> Value -> Target: Optional

Definitions:

Trigger? - A true/false value that determines the effects. If the trigger condition is met, then it executes the effect.
Action - The action to take.
Field - One of the card's values. Can be their attacking/endurance value.
Static - A static effect applied to the card.
Value - An integer number that determines how much the card is incremented/decremented by.
Target - Optional. Can be a specific card type.

Additional syntax:

/ - Or
& - And
"""


class Parser:
    def __init__(self, effect_string: str) -> None:
        """
        Initialises a parser instance.
        
        :param effect_string: The effect to parse.
        :type effect_string: str
        """

        self.effect_string = effect_string
        self.TRIGGERS = ["tap?", "summon?", "enter?", "attacking?", "blocking?", "discard?", "tapfor"]
        self.STATIC_ABILITIES = ["haste", "flying", "reach", "entertap", "unblockable", "trample", "invincible"]
        self.MODIFIERS = ["inc", "dec"]
        self.ACTIONS = ["gen", "draw", "discard", "heal", "return", "count", "damage", "destroy", "apply", "kill", "morph"]
    