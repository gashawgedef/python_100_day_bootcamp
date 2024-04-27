class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, Exhale")


def swim():
    print("Moving in water")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Under Water")


gashity = Fish()
swim()
gashity.breath()
print(gashity.num_eyes)
