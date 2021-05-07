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

clone = PurchaseClones.PurchaseClones

def test_purchase_clone():
   objs_returned = clone().purchase_clone(-1)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(pay().real_price(cloning)) 1', 'Clone(gestate().station_area()) 1' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone2():
   objs_returned = clone().purchase_clone2(-1)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(real_price(cloning).pay()) 1', 'Clone(station_area().gestate()) 1' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone_fail_Location():
   objs_returned = clone().purchase_clone(0)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) -1', 'Wallet(pay().real_price(cloning)) 0', 'Clone(gestate().station_area()) 0' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone_fail_Wallet():
   objs_returned = clone().purchase_clone(1)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(pay().real_price(cloning)) -1', 'Clone(gestate().station_area()) 0' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone_fail_Clone():
   objs_returned = clone().purchase_clone(2)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(pay().real_price(cloning)) 1', 'Clone(gestate().station_area()) -1' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone2_fail_Location():
   objs_returned = clone().purchase_clone2(0)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) -1', 'Wallet(real_price(cloning).pay()) 0', 'Clone(station_area().gestate()) 0' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone2_fail_Wallet():
   objs_returned = clone().purchase_clone2(1)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(real_price(cloning).pay()) -1', 'Clone(station_area().gestate()) 0' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone2_fail_Clone():
   objs_returned = clone().purchase_clone2(2)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(real_price(cloning).pay()) 1', 'Clone(station_area().gestate()) -1' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone_bad_failure_step():
   objs_returned = clone().purchase_clone(5)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(pay().real_price(cloning)) 1', 'Clone(gestate().station_area()) 1' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_purchase_clone2_bad_failure_step():
   objs_returned = clone().purchase_clone2(5)
   count = len(objs_returned)
   assert count == 3
   z = [ 'Location(is_in_area(clonevat)) 1', 'Wallet(real_price(cloning).pay()) 1', 'Clone(station_area().gestate()) 1' ]
   for idx, obj in enumerate(objs_returned):
      w =  obj.__class__.__name__ + '(' + obj.str + ') ' + str(obj.rc) 
      assert w == z[idx]

def test_methods():
   clone().is_in('vat')
   clone().is_in_area('vat')
   clone().pay(30)
   clone().price('vat')
   clone().gestate( 3 )
   clone().real_price('vat')
   clone().station_area()

