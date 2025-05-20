# def add_logging(cls):
#     class LoggedClass:
#         def __init__(self, *args, **kwargs):
#             self.wrapped = cls(*args, **kwargs)
#             print(f"Created: {self.wrapped}")
        
#         def __getattr__(self, name):
#             print(f"Accessing: {name}")
#             return getattr(self.wrapped, name)
#     return LoggedClass
# @add_logging
# class MyClass:
#     def hello(self):
#         print("Hello!")
# my_obj = MyClass()
# my_obj.hello()

# def add_say_hello(cls):
#     def say_hello(self):
#         return f"Hello from {self.__class__.__name__}!"
    
#     cls.say_hello = say_hello
#     return cls

# @add_say_hello
# class Person:
#     def __init__(self, name):
#         self.name = name

# p = Person("Abdul")
# print(p.say_hello()) 

# class DecoratorClass:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         print("Before function call")
#         result = self.func(*args, **kwargs)
#         print(result)
#         print("After function call")

# @DecoratorClass
# def my_function():
#     print("Inside function")

# @DecoratorClass
# def hello_name(name):
#     print(f"Hello, {name}!")
# my_function()
# hello_name("Abdul")

