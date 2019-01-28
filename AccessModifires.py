class A:
    def __init__(self, a):
        self.__a = a

    def setA(self, a):
        self.__a = a

    def display(self):
        print(self.__a)


aObj = A(10)

aObj.display()

aObj.__a = 20

print(aObj.__a)