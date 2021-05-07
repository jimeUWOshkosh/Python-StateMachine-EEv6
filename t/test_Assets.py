import os
import pytest
import lib.Assets         as Assets

class Dummy(object):
   def __init__(self):
      self.str = 'dummy'
      self.rc = 1

def test_classes():
    dummy = Dummy()
    Assets.Execute = 1;
    touch_obj    = Assets.Touch('file')
    area_obj     = Assets.Area(dummy)
    clone_obj    = Assets.Clone(dummy)
    location_obj = Assets.Location(dummy)
    wallet_obj   = Assets.Wallet(dummy)

    Assets.Execute = 1;
    touch_obj    = Assets.Touch('file')
    area_obj     = Assets.Area(dummy)
    clone_obj    = Assets.Clone(dummy)
    location_obj = Assets.Location(dummy)
    wallet_obj   = Assets.Wallet(dummy)

    os.remove('debug/file')


