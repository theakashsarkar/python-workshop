class File:
    path: str

    def read(self):
        pass
    
    def write(self):
        pass
    
    def getPath(self):
        return self.path

if __name__ == "__main__":
    file = File()
    file.read()
    # data escaping
    print(file.getPath())

class File:
    path: str

    def read(self):
        pass
    
    def write(self):
        pass
    
    def expose(self):
        print(self.path)

if __name__ == "__main__":
    file = File()
    file.read()
    file.expose()

    

