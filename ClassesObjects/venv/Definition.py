import random

class My_first_class:
    val1=random.choice([1,2,3,4,5,6,7,8,9])
    val2=random.choice([1,2,3,4,5,6,7,8,9])

    def Addem(self):
        return self.val1+self.val2

    def Getval1(self):
        print(self.val1)

    def Getval2(self):
        print(self.val2)

Obj1=My_first_class()
Obj1.Getval1()
Obj1.Getval2()
print(Obj1.Addem())

Obj2=My_first_class()
Obj2.Getval1()
Obj2.Getval2()
print(Obj2.Addem())