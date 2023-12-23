class First(object):
    def __init__ (self):
        super().__init__()
        print("first")

class Second(First):
    def __init__(self):
        super().__init__()
        print("second")

class Third(Second):
    def __init__(self):
        super().__init__()
        print("third")

a=Third()