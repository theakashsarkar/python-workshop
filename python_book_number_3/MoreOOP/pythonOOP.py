class Demo1: 
    def method(self):
        print('test2')
class Demo:
    def method(self):
        print('test')
        print(self)
demo = Demo()
# demo.method()
demo1 = Demo1()
# Demo.method(demo1)
# bound_method = Demo.__dict__['method'].__get__(demo, Demo)
# print(bound_method())
# demo.method(self=demo1)
Demo1.method()
# class Employee:
#     pass
# emp1 = Employee()
# emp1.first_name = "akash"
# emp1.last_name = "islam"
