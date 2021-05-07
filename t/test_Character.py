import pytest
import lib.Character         as Character

class Dummy(object):
   def __init__(self):
      self.str = 'dummy'
      self.rc = 1

def test_methods():
    character = Character.Character

    character().add(1)
    character().arm_wrestle(1)
    character().has_minimum_credits(1)
    character().is_in('vat')
    character().remove(1)
    character().show_balance()
    

