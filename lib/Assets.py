import os.path
from pathlib import Path

global Execute

class Touch(object):
   def __init__(self,file):
      self.str = 'touch'
      self.rc = 1
      Path('debug/' + file ).touch()

class Area(object):
   def __init__(self,obj):
#      print('Area ',end='')
#      print('\t', obj.__class__.__name__ + '().' + obj.str )
      self.str = obj.str
      obj.str = ''
      self.rc = 0
      if (Execute):
         # testing exceptions
         if os.path.isfile('debug/Assets.Area'):
            os.remove("debug/Assets.Area")
            print ("Area Failed")
            self.rc = -1
         else:
            self.rc = 1
#      else:
#         print("log only")
   def print_str(self):
      print(self.str)

class Clone(object):
   def __init__(self,clone):
#      print('Clone ',end='')
#      print('\t', clone.__class__.__name__ + '().' + clone.str )
      self.str = clone.str
      clone.str = ''
      self.rc = 0
      if (Execute):
         # testing exceptions
         if os.path.isfile('debug/Assets.Clone'):
            os.remove("debug/Assets.Clone")
            print ("Clone Failed")
            self.rc = -1
         else:
            self.rc = 1
#      else:
#         print("log only")
   def print_str(self):
      print(self.str)

class Location(object):
   def __init__(self,location):
#      print('Location ',end='')
#      print(location.__class__.__name__ + '().' + location.str )
      self.str = location.str
      location.str = ''
      self.rc = 0
      if (Execute):
         # testing exceptions
         if os.path.isfile('debug/Assets.Location'):
            os.remove("debug/Assets.Location")
            print ("Location Failed")
            self.rc = -1
         else:
            self.rc = 1
#      else:
#         print("log only")
   def print_str(self):
      print(self.str)

class Wallet(object):
   def __init__(self,obj):
#      print('Wallet ',end='')
#      print('\t', obj.__class__.__name__ + '().' + obj.str )
      self.str = obj.str
      obj.str = ''
      self.rc = 0
      if (Execute):
         # testing exceptions
         if os.path.isfile('debug/Assets.Wallet'):
            os.remove("debug/Assets.Wallet")
            print ("Wallet Failed")
            self.rc = -1
         else:
            self.rc = 1
#      else:
#         print("log only")
#      print(self.rc)

   def print_str(self):
      print(self.str)
