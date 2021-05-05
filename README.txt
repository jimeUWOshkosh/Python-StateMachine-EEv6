Simple State Machine in python

Take an Economic Exchange Code Block written in python as input to a filter program
and create a Simple State machine code for a python method for a class.

There is a mdp presentation that further explains this project.

---
This topic is due to generosity of Curtis 'Ovid' Poe (Tau Station, 
All Around the World)

Person:==================  https://ovid.github.io/    
Company:=================  https://allaroundtheworld.fr/
His Company's MMORP Game:  https://taustation.space/

Purchase his books
   Beginning Perl
   Perl Hacks

Articles/Video on the Subject by Mr. Poe and company
   Modeling a Universe (Video) [Aug 2017]
      https://www.youtube.com/watch?v=UmLwYLSmTSs&feature=emb_imp_woyt
   Modeling a Universe (Video) [Nov 2017]
      https://www.youtube.com/watch?v=UmLwYLSmTSs`
   On Writing Clean Code [April 2017]
      https://taustation.space/blog/on-writing-clean-code/
   Writing Declarative Perl [June 2017]
      http://blogs.perl.org/users/ovid/2017/06/writing-declarative-perl.html
   Writing Declarative Perl (different code examples) [March 2021]
      https://dev.to/ovid/writing-declarative-software-375o
   On Writing Clean Code for Combat [February 2018]
      https://taustation.space/blog/on-writing-clean-code-for-combat/
   Extending Economic Exchange Condtions [April 2018]
     https://taustation.space/blog/extending-economic-exchange-conditions/
   Making Complex Software Simple [April 2020]
     https://taustation.space/blog/making-complex-software-simple/
   
---
Library
   Assets
      Classes for Area,Clone,Location,Wallet
         Just stub classes to handle logging and testing for Asset Failure
   Character
      Define methods for a character
   Challenge
      Only one challenge defined at the time. Has a state machine for
      a Arm Wrestling challenge. (method: arm_wrestling_challenge)
   PurchaseClones
      Has two state machines that handle different ways to execute
      creating a clone. 1st (method: purchase_clone) uses Subject,
      Verb, Object argument list. 2nd (method: purchase_clones2) uses
      method chaining.

run.py  
   A simple program that executes 1) create a couple of clones
   2) a arm wrestling challenge

my-py-filter.py
   A source filter that takes an EconomicExchange Code Block and
   outputs a state machine code to handle the step transcation.
---


├── EEcodeblocks                 EconomicExchange code blocks
│   ├── step.clone.doc           codeblock using Subject,Verb,Object argument list
│   ├── step.clone.chain.doc     codeblock using chaining of methods
│   ├── multi.step.doc           a list of all the code blocks in python
│   ├── multi.step.txt           a list of all the code blocks in perl
│   ├── step.awc.doc             codeblock using SVO arg list for Arm Wrestling Challenge
│   └── step.scavenge.doc        codeblock NOT use, for a "Search for salvageable goods"
├── lib
│   ├── Assets.py                Classes for Assets
│   ├── Challenge.py             Challenges for a player (currently only Arm Wrestling) [State Machine]
│   ├── Character.py             Class for Character def
│   └── PurchaseClones.py        Purchase of a Clone (two choices) [State Machine]
├── my-py-filter.pl              Source code filter program
├── Perl.source.filter.txt       Example of before and after in perl data structure wise
├── run.py                       Runs the example program
├── talk.mdp                     MDP presentation of the project
├── debug                        Sub Dir for helping in testing of an Asset's constructor method failing
└── tmp                          Some Notes along the way
    ├── noStateMachine.example.pl
    ├── t1.py
    └── t2.py
