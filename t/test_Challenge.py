#import sys
#import os, pathlib

# Add the project's root directory to the system path
#sys.path.append(str( cwd.parent ))

# This is optional, but you can add a lib directory
# To the system path for tests to be able to use
#sys.path.append(str( cwd / '../lib' ))
import pytest
import lib.Assets         as Assets
import lib.Character      as Character
import lib.PurchaseClones as PurchaseClones
import lib.Challenge      as Challenge

def test_function1():
   character = Character.Character
   challenge = Challenge.Challenge
   objs_returned = challenge().arm_wrestling_challenge(character,-1)
   count = len(objs_returned)
   assert count == 6
   output1 = [ 'Area(is_in(inn)) 1', 'Wallet(has_minimum_credits( 97)) 1', 'Location(arm_wrestle( 33)) 1',
           'Wallet(add( 97)) 1', 'Wallet(remove(amount)) 0', 'Wallet(show_balance()) 1']
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == output1[idx]

