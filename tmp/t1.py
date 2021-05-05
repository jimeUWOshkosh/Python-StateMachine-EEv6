class Foo(object):
    def bar(self):
        print "Foo.bar called"
        return self
    def baz(self):
        print "Foo.baz called"
        return self
foo = Foo()
foo2 = foo.bar().baz()
print " id(foo):", id(foo)
print "id(foo2):", id(foo2)
