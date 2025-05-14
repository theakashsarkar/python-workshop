
class A:
  def fnc(self):
    print("Hello World")
class B:
  def fnc(self):
    print("Hello class b")
  def method_b(self):
    print("Method b")
class C(A, B):
  def fnc(self):
    print("Hello class c")
  # def method_b(self):
  #   print("Method b")
class D(B, C):
  pass
d = D()
d.fnc()
# c = C()
# c.fnc()