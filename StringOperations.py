'''
    Define a class which has following methods:
    getString: to get a string from console input
    printString: to print the string.
    printStringInUpper: to print string in upper case
    removeDigits: to remove digits from the string and print the resultant string.
'''

from string import digits

class String:
    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input('Enter any string: ')
    
    def printString(self):
        print(self.string)

    def printStringInUpper(self):
        print(self.string.upper())

    def removeDigits(self):
        i = 0
        while i < len(self.string):
            char = self.string[i]
            if ord(char) >= 48 and ord(char) <= 57:
                self.string = self.string.replace(char, '')
            else:
                i += 1


s = String()

s.getString()
s.printString()
s.printStringInUpper()
s.removeDigits()
s.printString()

