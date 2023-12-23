class A:
    def explore(self):
        print("I'm exploring A")

class B(A):
    def explore (self, place=None):
        if place is not None:
            print("I'm exploring",place)
        else:
            super().explore()

b=B()
b.explore("Jakarta")
b.explore()