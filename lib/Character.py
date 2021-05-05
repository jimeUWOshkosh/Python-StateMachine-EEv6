import sys

class Character(object):
   def __init__(self):
      self.str = ''

   def add(self,amt):
      self.str = "add( " + str(amt) + ")"
      return self

   def arm_wrestle(self,npc):
      self.str = "arm_wreslte( " + str(npc) + ")"
      return self

   def has_minimum_credits(self,amt):
      self.str = "has_minimum_credits( " + str(amt) + ")"
      return self

   def is_in(self,place):
      self.str = "is_in(" + place + ")"
      return self

   def remove(self,amount):
      self.str = 'remove(amount)'
      return self

   def show_balance(self):
      self.str = 'show_balance()'
      return self
