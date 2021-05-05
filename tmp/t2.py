behaviors0 = [ 'NONE', 'NONE', 'NONE', 'FAILURE', 'ALWAYS' ]

lastidx = 0
#for idx , val in enumerate(behaviors0,start=(lastidx+1)):
for idx , val in enumerate(behaviors0,):
   if (idx <= lastidx):
      print(idx)
      pass
   if ( (val == 'FAILURE') or (val == 'ALWAYS') ):
      print('\t',idx)

