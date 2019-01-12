# 1. String

var1 = "This is my String"

# 'Codekul' - The "Gurukul" for Coders!

var2 = """'Codekul' - The "Gurukul" for Coders!"""

'''
\n
\t
\b
\r
'''
var3 = "Codekul\rThe Gurukul for Coders!"

var4 = """Codekul
    The Gurukul
    for Coders!"""

a = 10
b = 20.40
# print("Value of a: %d\nValue of b: %f" % (a, b))


# print('Value of a: {}\nValue of b: {}'.format(a, b))

var5 = 'This is my String'

var5 = var5.replace('i', 'a')


# print(var5)
# 2. List
myList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Red', 'Green', 'Blue', 30.799]

myList1.append(True)


myList2 = myList1 + ['One', 'Two']
# print(myList2)

# for char in var5:
#     print(char)


# for i, a in enumerate(myList2):
#     print(a)
#     if i == 6:
#         break

# 3. Dictionary

d1 = {"key1": "Value1"}

d2 = {1: "One", 2: "Two", 3: "Three",
      4: "Four", 'Five': 5, 'Six': 6, 'Seven': 7, 8: 80}
print(d2['Five'])

# 4. Tuple

t1 = (1, 2, 3, 4, 5)

# print(t1[3])
