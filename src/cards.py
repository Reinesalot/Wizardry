class Card:
     def __init__(self, name: str, generic_mana: int, sp_mana: str, card_type: str, description: str, effect: str) -> None:
          """
          Parent class for type Card.

          :param name: Name of the card.
          :type name: str
          :param generic_mana: Any coloured mana cost.
          :type generic_mana: int
          :param sp_mana: Coloured mana type.
          :type sp_mana: str
          :param card_type: The card type - can be a Land/Creature/Spell/Enchant.
          :type card_type: str
          :param description: The description of the card.
          :type description: str
          :param effect: The card's effects scripted in custom syntax.
          :type effect: str
          """
          self.name = name
          self.generic_mana = generic_mana
          self.sp_mana = sp_mana
          self.card_type = card_type
          self.description = description
          self.effect = effect
          self.tapped = 0     # 0 for untapped, 1 for tapped
          self.statuses = []
          self.id = 0
     def to_dict(self) -> dict:
          """
          Returns a dictionary representation of the card.

          :rtype: dict
          """
          return {
               "id": str(self.id),
               "name": self.name,
               "generic_mana": self.generic_mana,
               "sp_mana": self.sp_mana,
               "type": self.type,
               "description": self.description,
               "tapped": self.tapped,
               "status": self.status,
               "effect": self.effect
          }
     
class CreatureCard(Card):
     def __init__(self, name: str, generic_mana: int, sp_mana: int, description: str, att: int, end: int, effect: str) -> None:
          """
          Initialises a Creature Card.
          
          :param name: Name of the card.
          :type name: str
          :param generic_mana: Any coloured mana cost.
          :type generic_mana: int
          :param sp_mana: Coloured mana type.
          :type sp_mana: int
          :param description: The description of the card.
          :type description: str
          :param att: The creature's attack value.
          :type att: int
          :param end: The creature's defence value.
          :type end: int
          :param effect: The card's effects scripted in custom syntax.
          :type effect: str
          """
          super().__init__(name, generic_mana, sp_mana, "Creature", description)
          self.attack = att
          self.defence = end
     
     def to_dict(self) -> dict:
          """
          Returns a dictionary representation of the card.
          
          :rtype: dict
          """
          data = super().to_dict()
          data.update(
               {
                    "attack": self.attack,
                    "defence": self.defence,
               }
          )
          return data