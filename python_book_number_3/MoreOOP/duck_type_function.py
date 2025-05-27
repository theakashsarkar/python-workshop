class A:
    def get_method_reference(self):
        func = self.do_something.__func__
        print(func)
        return func
    def do_something(self):
        print(f"{type(self).__name__} is doing something")
class B:
    def do_something(self):
        print(f"{type(self).__name__} is doing somethings in B's way")

a = A()
b = B()

method_func = a.get_method_reference()
method_func(b)