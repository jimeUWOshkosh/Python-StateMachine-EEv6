import sys
import lib.Assets as Assets

class Challenge(object):
 
   def __init__(self):
      self.str = ''

   def arm_wrestling_challenge(self,character):
      bet_amount = 0
      npc = 0

      def steps0(option):
        if option == 0:
          return   Assets.Area(     character().is_in('inn') )
        elif option == 1:
          return   Assets.Wallet(   character().has_minimum_credits(bet_amount) )
        elif option == 2:
#          zz = Assets.Touch('Wallet')
          return   Assets.Location( character().arm_wrestle(npc) )
        elif option == 3:
#          zz = Assets.Touch('Wallet')
          return   Assets.Wallet(   character().add(bet_amount) )
        elif option == 4:
          return   Assets.Wallet(   character().remove(bet_amount)                 ) 
        elif option == 5:
          return   Assets.Wallet(   character().show_balance()                     ) 
        else:
           print("Incorrect option")

      behaviors0 = [ 'NONE','NONE','NONE','NONE','FAILURE','ALWAYS' ]
      returned = []

      lastidx = 0
      Assets.Execute = True    # whether an Asset is executed or log only
      err = False
      for idx , val in enumerate(behaviors0):
         lastidx = idx
         if (val != 'FAILURE'):
            Assets.Execute = True
            obj = steps0(idx)
            returned.append(obj)
            if (obj.rc < 0):
               err = True
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
         x=1
         # log the FAILUREs
         for i in range(len(returned)):
            if (returned[i].rc == 0):
               Assets.Execute = False
               returned[i] = steps0(i)

      print('in discover')
      for idx, obj in enumerate(returned):
          print( obj.__class__.__name__ + '().' + obj.str + ' ' + str(obj.rc) )

      print("------------------")
      return returned


