# array = []

# while(True):
#     input1 = input("Enter a number")
#     number = int(input1)
#     array.append(number)
#     if len(array) >= 5:
#         print(array) 
#         array = []

class AlphabetStore:

    def __init__(self):
        self.array = []

    def take_input(self):
        input1 = int(input("Enater a number"))
        self.add_to_array(input1)

    def add_to_array(self, input):
        self.array.append(input)
        if len(self.array) >= 5:
            self.print_and_flush()
            
    def print_and_flush(self):
        print(self.array)
        self.array = []

#  generate a object from blueprint

if __name__ == "__main__":
    alphabetStore = AlphabetStore()
    while True:
        alphabetStore.take_input()
