class MyClass:

    my_num = 0
    def __init__(self):
        print('Initializer')
        self.my_num = 10

    def set_my_num(self, num):
        self.my_num = num

    def get_my_num(self):
        return self.my_num

my_object = MyClass()
# my_object.set_my_num(20)
print(my_object.get_my_num())





