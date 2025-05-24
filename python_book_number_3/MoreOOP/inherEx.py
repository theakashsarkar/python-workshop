# class Green():
#     def getColor(self):
#         print("get color green")

# class Blue(Green):
#     def getColor(self):
#         print("get color blue")

# if __name__ == "__main__":
#     green: Green = Blue()
#     green.getColor()

from typing import Protocol
class Icolor:
    def getColor():
        pass

class Green:
    def getColor(self):
        print("color green")

class Blue:
    def getColor(self):
        print("color blue")

if __name__ == "__main__":
    color: Icolor = Blue()
    color.getColor()

# class ICommon():
#     def wheele():
#         pass
#     def brack():
#         pass
#     def horn():
#         pass
#     def carryHalmat():
#         pass


# class Cyclie(ICommon):
#     pass

# class Scooty(ICommon):
#     pass