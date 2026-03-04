import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.modules.parser import *
from src.modules.utils import *
from src.cards import *

<<<<<<< Updated upstream
=======
forest_bear = CreatureCard(
    name="Forest Bear",
    generic_mana=1,
    sp_mana="green",
    description=(
        "A powerful bear from the deep forest."
        "|Why does he look like a dog"
    ),
    att=2,
    end=2,
    effect="haste",
)

new_card = update_card(forest_bear, {""}, "player")
print(new_card.to_dict())
>>>>>>> Stashed changes

