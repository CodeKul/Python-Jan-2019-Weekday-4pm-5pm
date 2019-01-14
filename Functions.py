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