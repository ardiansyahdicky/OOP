from turtle import Shape

class Square(Shape):
    name="square"
    width=0         #A default value

    def __init__(self, width):
        self.width=width

    def get_area(self):
        return self.width*self.width

    @classmethod
    def input(self):
        sq_width=int(input("Masukkan angka 5 sbg sisi: "))
        return self(sq_width)

squareX=Square.input()
print('Luas perseginya: ',squareX.get_area())

class Triangle(Shape):
    name="Triangle"
    width=0
    height=0

    def __init__(self, width, height):
        self.width=width
        self.height=height

    def get_area(self):
        return 0.5*self.width*self.height

    @classmethod
    def user_input(self):
        a=self.width, self.height
        tri_width=int(input("Masukkan angka 5 sbg tinggi: "))
        tri_height=int(input("Masukkan angka 3 sbg alas: "))
        return self(tri_width, tri_height)

triangleY=Triangle.user_input()
print('Luas segitiganya: ',triangleY.get_area())