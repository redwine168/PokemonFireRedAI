
class Pokemon:

    def __init__(self, name, typeOne, typeTwo):
        self.Name = name
        self.TypeOne = typeOne
        self.TypeTwo = typeTwo

    def __str__(self):
        return self.Name + ": " + self.TypeOne + ", " + self.TypeTwo
