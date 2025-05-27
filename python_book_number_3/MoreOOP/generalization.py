from typing import Protocol

class IWritable(Protocol):
    def write():
        pass

class IErasable(Protocol):
    def erase():
        pass

class Pencil:
    def write(self):
        print("writing with pencil")
    def erase(self):
        print("Erasing with a pencil")

class Pen:
    def write(self):
        print("write with pen")

if __name__ == "__main__":
    pen: IWritable = Pen()
    pencil: IWritable  = Pencil()
    erasablePencil: IErasable = Pencil()

    pen.write()
    pencil.write()
    erasablePencil.write()

    

    class Pen():
        def write(self):
            print('Writing with pen')
    class Pencil(Pen):
        def write(self):
            print('Write with pencil')
        def erase(self):
            print('erase with pencil')
    