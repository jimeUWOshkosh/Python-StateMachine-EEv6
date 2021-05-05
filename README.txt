Simple State Machine in python

Take an Economic Exchange Code Block written in python as input to a filter program
and create a Simple State machine code for a python method for a class.

There is a mdp presentation that further explains this project.


├── debug
├── EEcodeblocks                 EconomicExchange code blocks
│   ├── step.clone.doc           codeblock using Subject,Verb,Object argument list
│   ├── step.clone.chain.doc     codeblock using python's chaining of methods
│   ├── multi.step.doc           a list of all the code blocks in python
│   ├── multi.step.txt           a list of all the code blocks in perl
│   ├── step.awc.doc             codeblock using SVO arg list for Arm Wrestling Challenge
│   └── step.scavenge.doc        codeblock NOT use, for a "Search for salvageable goods"
├── lib
│   ├── Assets.py                 Classes for Assets
│   ├── Challenge.py              Challenges for a player (currently only Arm Wrestling) [State Machine]
│   ├── Character.py              Class for Character def
│   └── PurchaseClones.py         Purchase of a Clone (two choices) [State Machine]
├── my-py-filter.pl               Source code filter program
├── Perl.source.filter.txt        Example of before and after in perl data structure wise
├── run.py                        Runs the example program
├── talk.mdp                      MDP presentation of the project
└── tmp                           Some Notes along the way
    ├── noStateMachine.example.pl
    ├── t1.py
    └── t2.py
