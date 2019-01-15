def function_name():
    print('This is my first functions')

function_name()


def fuction_with_param(name):
    print('Name: {}'.format(name))


fuction_with_param('Codekul')


def function_with_multi_param(a, b, c, d):
    print('a: {} b: {} c: {} d: {}'.format(a,b,c,d))


function_with_multi_param(1, 80.67, True, 'Python')


def function_with_default_param(name=10):
    print(name)

function_with_default_param('Heena')


def function_with_returning_value():
    return "Codekul"


var = function_with_returning_value()
print(var)


def addition(a,b):
    c = a + b
    return c

res = addition(10, 20)
print('Calculation: {}'.format(res))


def is_even(num):
    if num % 2 == 0:
        return '{} is even'.format(num)
    else:
        return '{} is odd'.format(num)


print(is_even(15))


def display_number(num):
    print('address of num: {}'.format(id(num)))
    num = 200
    print('after change address of num: {}'.format(id(num)))
    print(num)

my_num = 100
print('address of my_num: {}'.format(id(my_num)))
display_number(my_num)
print(my_num)


def display_list(list):
    print('address of list: {}'.format(id(list)))
    list = [4,5,6]
    print('after change address of list: {}'.format(id(list)))
    print(list)


my_list = [1,2,3]
print('address of my_list: {}'.format(id(my_list)))
display_list(my_list)
print(my_list)


def swap_two_values(a, b):
    temp = a
    a = b
    b = temp
    print('x: {}\ny: {}'.format(a, b))


x = 10
y = 20
swap_two_values(x, y)

