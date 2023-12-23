class Person:
     def __init__(self, name, age):
         self.name=name
         self.age=age

     def data(self):
         return self.name+' umurnya '+self.age+' tahun'

     @classmethod
     def user_input(self):
            name=input('Masukkan nama: ')
            age=input('Masukkan umur: ')
            return self(name, age)

person1=Person.user_input()
print(person1.data())