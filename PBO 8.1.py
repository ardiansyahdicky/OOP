class Hasan:
    surname = "Hasan"
    profession = "Engineer"

    def __init__ (self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession=profession