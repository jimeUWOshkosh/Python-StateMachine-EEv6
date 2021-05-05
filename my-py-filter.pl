#!/usr/bin/env perl
use strict; use warnings; use feature 'say';

my $found = 0;
my $current_step = 0;
my $current_state_machine = 0;
my $elif_flag = 0;
my @behaviors;
while (<>) {
    chomp;
    if (not $found) {
        if (/Steps\(/) {
            $found = 1;
	    $elif_flag = 0;
            $current_step= 0;
#==========TOP OF STATE MACHINE================================================
            my $code0 = <<"CODE0";
      def steps$current_state_machine(option):
CODE0
	    print $code0;
#===END OF TOP OF STATE MACHINE================================================
        } else {
            say;
        }
    } else {
        if (/#STEPS/) {
	    $found = 0;
	    my $str = join(",",@behaviors);
#==========BOTTOM OF STATE MACHINE=============================================
            my $code1 = <<"CODE1";
        else:
           print("Incorrect option")

      behaviors${current_state_machine} = [ ${str} ]
      returned = []

      lastidx = 0
      Assets.Execute = True    # whether an Asset is executed or log only
      err = False
      for idx , val in enumerate(behaviors${current_state_machine}):
         lastidx = idx
         if (val != 'FAILURE'):
            Assets.Execute = True
            obj = steps${current_state_machine}(idx)
            returned.append(obj)
            if (obj.rc < 0):
               err = True
               break   # err
         else:
            # log the FAILURE's info into the object
            Assets.Execute = False
            returned.append(steps${current_state_machine}(idx))

      if (err):
         # check if there are any FAILUREs we skipped before ERR
         for i in range(len(returned)):
            if (returned[i].rc == 0):
               Assets.Execute = True
               returned[i] = steps${current_state_machine}(i)

         # for the steps after idx, Execute FAILUREs and ALWAYSs, log the rest
         for idx , val in enumerate(behaviors${current_state_machine}):
            if (idx > lastidx):
               if ( (val == 'FAILURE') or (val == 'ALWAYS') ):
                  Assets.Execute = True
                  returned.append(steps${current_state_machine}(idx))
               else:
                  Assets.Execute = False
                  returned.append(steps${current_state_machine}(idx))
      else:  # No ERR
         # log the FAILUREs' info into the object
         Assets.Execute = False
         for i in range(len(returned)):
            if (returned[i].rc == 0):
               returned[i] = steps${current_state_machine}(i)

      print('in discover')
      for idx, obj in enumerate(returned):
          print( obj.__class__.__name__ + '().' + obj.str + ' ' + str(obj.rc) )

      print("------------------")
      return returned


CODE1
	        $current_state_machine++;
		@behaviors = ();
	        print $code1;
#===END OF BOTTOM OF STATE MACHINE=============================================
        } else {
	    if (not $elif_flag) {
	        $elif_flag = 1;
#==========FIRST STATE=========================================================
            my $code2a = <<"CODE2A";
        if option == $current_step:
CODE2A
	        print $code2a;
#===END OF FIRST STATE=========================================================
	    } else {
#==========REST OF STATES======================================================
            my $code2b = <<"CODE2B";
        elif option == $current_step:
CODE2B
	        print $code2b;
#===END OF REST OF STATES======================================================
	    }
	    #
	    # EACH STEP
	    #
	    #
	    # A STEP WITH A BEHAVIOR
            if (/(?<post_trans>FAILURE|ALWAYS|ASSERT)(\()(?<rest>\N.*)(\))\s*,\s*\z/) {
		my $rest = $+{rest};
		my $post_trans = $+{post_trans};
		$rest =~  s/^\s+//g;   # trim left
	        say "          return   ",$rest;
		push(@behaviors, "\'${post_trans}\'");
	    } else {
	    # A STEP WITHOUT A BEHAVIOR
		$_ =~  s/^\s+//;    # trim left
		$_ =~  s/,\s*\z//;  # trim comma
	        say "          return   ",$_;
		push(@behaviors, "\'NONE\'");
	    }
            $current_step++;
        }
    }
}
