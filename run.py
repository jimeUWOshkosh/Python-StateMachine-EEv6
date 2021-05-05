import sys
from pathlib import Path

import lib.Assets         as Assets
import lib.Character      as Character
import lib.PurchaseClones as PurchaseClones
import lib.Challenge      as Challenge

# Purchase a clone using Ovid's SVO
#Path('debug/Wallet').touch()
clone = PurchaseClones.PurchaseClones
objs_returned = clone().purchase_clone()

# using Python's chaining methods
#Path('debug/Wallet').touch()
clone2 = PurchaseClones.PurchaseClones
objs_returned = clone2().purchase_clone2()

# Use accept a Challenge to arm wrestle using Ovid's SVO
#Path('debug/Wallet').touch()
character = Character.Character
challenge = Challenge.Challenge
objs_returned = challenge().arm_wrestling_challenge(character)


