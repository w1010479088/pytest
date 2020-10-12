class Fish:

    def __init__(self):
        self.hungry = True
        self.name = ""

    def eat(self, food):
        if food is not None:
            self.hungry = False

    def rename(self, name):
        if name is not None:
            self.name = name
