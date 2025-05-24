from typing import Protocol

class Istudent:
    def nightPrep():
        pass

class ResidentialStudent:
    def nightPrep(self):
        print("hall read")

class NonResidentialStudent:
    def nightPrep(self):
        print("Home read")

if __name__ == "__main__":
    akash: Istudent = ResidentialStudent()
    # akash: ResidentialStudent = NonResidentialStudent()
    naswan: Istudent = NonResidentialStudent()
    akash.nightPrep()