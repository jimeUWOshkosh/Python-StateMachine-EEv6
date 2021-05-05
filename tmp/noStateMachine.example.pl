use feature 'say';
sub one {
   say('one');
}
sub two {
   say('two');
}
sub three {
   say('three');
}
sub four {
   say('four');
}
sub steps {
   say('steps');
}

steps( two( one('stuff')),
       four(three('more stuff')));

