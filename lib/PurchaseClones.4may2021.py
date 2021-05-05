import sys
import lib.Assets    as Assets
import lib.Character as Character

class PurchaseClones(object):
   chaining = False 
   def __init__(self):
      self.str = ''

   def is_in(self,location):
      self.str = 'is_in_area(' + location + self.str + ')'
      return self

   def is_in_area(self,location):
      self.str = 'is_in_area(' + location + self.str + ')'
      return self

   def pay(self,arg1):
      if (self.chaining):
         self.str = self.str + 'pay()' 
      else:
         self.str = 'pay()' + self.str
      return self

   def price(self,location):
      if (self.chaining):
         self.str = self.str + 'price()' 
      else:
         self.str = 'price()' + self.str
      return self

   def gestate(self,arg1):
      self.str = 'gestate()' + self.str
      return self

   def real_price(self,location):
      self.str = 'real_price()'
      return self

   def station_area(self):
      self.str = 'station_area()' + self.str
      return self

   def purchase_clone(self):

      def steps0(option):
        if option == 0:
#          return   Assets.Touch('Wallet')
          return   Assets.Area(   self.is_in('clonevat')                   )
        elif option == 1:
          return   Assets.Wallet( self.pay( self.real_price('cloning') ) )
        elif option == 2:
          return   Assets.Area(   self.is_in('clonevat')                   )
          return   Assets.Clone(  self.gestate( self.station_area() )    )
        else:
           print("Incorrect option")

      behaviors0 = [ 'NONE','NONE','NONE' ]
      returned = []

      lastidx = 0
      Assets.Execute = True    # whether an Asset is executed or log only
      err = False
      for idx , val in enumerate(behaviors0):
         lastidx = idx
         if (val != 'FAILURE'):
            obj = steps0(idx)
            returned.append(obj)
            if (obj.rc < 0):
               err = True
               Assets.Execute = False
               break   # err
         else:
            Assets.Execute = False
            returned.append(steps0(idx))

      if (err):
         # check if there are any FAILUREs we skipped before ERR
         for i in range(len(returned)):
            if (returned[i].rc == 0):
               Assets.Execute = True
               returned[i] = steps0(i)

         # for the steps after idx, Execute FAILUREs and ALWAYSs, log the rest
         for idx , val in enumerate(behaviors0):
            if (idx > lastidx):
               if ( (val == 'FAILURE') or (val == 'ALWAYS') ):
                  Assets.Execute = True
                  returned.append(steps0(idx))
               else:
                  Assets.Execute = False
                  returned.append(steps0(idx))
      else:  # No ERR
         # log the FAILUREs
         for i in range(len(returned)):
            if (returned[i].rc == 0):
               Assets.Execute = True
               returned[i] = steps0(i)

      print('in discover')
      for idx, obj in enumerate(returned):
          print( obj.__class__.__name__ + '().' + obj.str + ' ' + str(obj.rc) )

      print("------------------")
      return returned





   def purchase_clone2(self):
      self.chaining = True
      Assets.Execute = True
      arg1=0

      def steps0(option):
        if option == 0:
          return   Assets.Location( self.is_in_area('clonevat') )
        elif option == 1:
          return   Assets.Wallet(   self.price('cloning').pay(arg1)  )
        elif option == 2:
          return   Assets.Clone(   self.station_area().gestate(arg1) )
        else:
           print("Incorrect option")

      behaviors0 = [ 'NONE','NONE','NONE' ]
      returned = []

      lastidx = 0
      Assets.Execute = True    # whether an Asset is executed or log only
      err = False
      for idx , val in enumerate(behaviors0):
         lastidx = idx
         if (val != 'FAILURE'):
            obj = steps0(idx)
            returned.append(obj)
            if (obj.rc < 0):
               err = True
               Assets.Execute = False
               break   # err
         else:
            Assets.Execute = False
            returned.append(steps0(idx))

      if (err):
         # check if there are any FAILUREs we skipped before ERR
         for i in range(len(returned)):
            if (returned[i].rc == 0):
               Assets.Execute = True
               returned[i] = steps0(i)

         # for the steps after idx, Execute FAILUREs and ALWAYSs, log the rest
         for idx , val in enumerate(behaviors0):
            if (idx > lastidx):
               if ( (val == 'FAILURE') or (val == 'ALWAYS') ):
                  Assets.Execute = True
                  returned.append(steps0(idx))
               else:
                  Assets.Execute = False
                  returned.append(steps0(idx))
      else:  # No ERR
         # log the FAILUREs
         for i in range(len(returned)):
            if (returned[i].rc == 0):
               Assets.Execute = True
               returned[i] = steps0(i)

      print('in discover')
      for idx, obj in enumerate(returned):
          print( obj.__class__.__name__ + '().' + obj.str + ' ' + str(obj.rc) )

      print("------------------")
      return returned
