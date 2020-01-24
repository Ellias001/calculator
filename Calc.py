from tkinter import *

class Calculator(Button):

    def __init__(self, fnum = '', isDelete = 0, isFirst = 0, isDecimal = 0, \
                 isBracket = 0, numOfBrackets = 0):
        self.fnum = fnum
        self.isDelete = isDelete
        self.isFirst = isFirst
        self.isDecimal = isDecimal
        self.isBracket = isBracket
        self.numOfBrackets = numOfBrackets

    def clickButton(self, entity, symbol):
        current = str(entity.get())
        entity.delete(0, END)
        self.isFirst = 0
        
        if((current == '' or self.isDelete == 1) and symbol == '.'):
            current = '0'
            
        if(symbol == ')' and self.isBracket == 0):
            entity.insert(0, 'Wrong Syntax')
            self.isDelete = 1
            return
        elif(symbol == ')'):
            print(0)
            if(self.numOfBrackets <= 0 and current[-1] == '('):
                entity.delete(0, END)
                entity.insert(0, 'Wrong Syntax')
                self.isDelete = 1
                return
            elif(self.numOfBrackets <= 0):
                current = '(' + current
            else:
                self.numOfBrackets -= 1

        if(symbol == '('):
            self.numOfBrackets += 1
            self.isBracket = 1

        if(self.isDelete):
            if(symbol == '.'):
                entity.insert(0, current + '.')
                self.isDecimal = 1
                self.isDelete = 0
            else:
                entity.insert(0, symbol)
                self.isDelete = 0
        else:
            if(self.isDecimal and symbol == '.'):
                entity.insert(0, 'Wrong Syntax')
            elif(not(self.isDecimal) and symbol == '.'):
                entity.insert(0, current + '.')
                self.isDecimal = 1
            else:
                entity.insert(0, current + symbol)

    def clearEntry(self, entity):
        entity.delete(0, END)
        self.fnum = ''
        self.__init__()

    def delete(self, entity):
        if(len(str(e.get())) > 0):
            val = str(entity.get())[:-1]
            self.isDelete = 0
            if(str(entity.get())[-1] == '.'):
                self.idDecimal = 0
            entity.delete(0, END)
            entity.insert(0, val)
            

    def calcFunction(self, entity, sign):
        current = str(entity.get())
        if (self.isFirst):
            self.isFirst = 1
            return

        if(current == ''):
            current = '0'

        if(self.isBracket):
            entity.delete(0, END)
            entity.insert(0, current + sign)
            return
        
        self.isDelete = 1
        self.isDecimal = 0
        self.fnum = str(eval(self.fnum + current)) + sign
        entity.delete(0, END)
        entity.insert(0, self.fnum[:-1])

    def equal(self, entity):
        current = str(entity.get())
        if(self.isBracket):
            for i in range(self.numOfBrackets):
                current = current + ')'
            current = str(eval(current))
            numOfBrackets = 0

        entity.delete(0, END)
        entity.insert(0, eval(self.fnum + current))
        self.__init__()
        self.isDelete = 1

root = Tk()
root.title("Calculator")

calc = Calculator()

# Defining and placing entry
e = Entry(root, width = 50, borderwidth = 15)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# Defining buttons
openBracketButton = Button(root, text = "(", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '('))
closeBracketButton = Button(root, text = ")", padx = 40, pady = 20, command = lambda: calc.clickButton(e, ')'))
deleteButton = Button(root, text = "<", padx = 40, pady = 20, command = lambda: calc.delete(e))
clearButton = Button(root, text = "C", padx = 40, pady = 20, command = lambda: calc.clearEntry(e))

sevenButton = Button(root, text = "7", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '7'))
eightButton = Button(root, text = "8", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '8'))
nineButton = Button(root, text = "9", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '9'))
plusButton = Button(root, text = "+", padx = 40, pady = 20, command = lambda: calc.calcFunction(e, '+'))

fourButton = Button(root, text = "4", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '4'))
fiveButton = Button(root, text = "5", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '5'))
sixButton = Button(root, text = "6", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '6'))
minusButton = Button(root, text = "-", padx = 40, pady = 20, command = lambda: calc.calcFunction(e, '-'))

oneButton = Button(root, text = "1", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '1'))
twoButton = Button(root, text = "2", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '2'))
threeButton = Button(root, text = "3", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '3'))
mullButton = Button(root, text = "*", padx = 41, pady = 20, command = lambda: calc.calcFunction(e, '*'))

zeroButton = Button(root, text = "0", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '0'))
pointButton = Button(root, text = ".", padx = 40, pady = 20, command = lambda: calc.clickButton(e, '.'))
equalButton = Button(root, text = "=", padx = 40, pady = 20, command = lambda: calc.equal(e))
divideButton = Button(root, text = "/", padx = 40, pady = 20, command = lambda: calc.calcFunction(e, '/'))

# Placing Buttons on the screen
openBracketButton.grid(row = 1, column = 0)
closeBracketButton.grid(row = 1, column = 1)
deleteButton.grid(row = 1, column = 2)
clearButton.grid(row = 1, column = 3)

sevenButton.grid(row = 2, column = 0)
eightButton.grid(row = 2, column = 1)
nineButton.grid(row = 2, column = 2)
plusButton.grid(row = 2, column = 3)

fourButton.grid(row = 3, column = 0)
fiveButton.grid(row = 3, column = 1)
sixButton.grid(row = 3, column = 2)
minusButton.grid(row = 3, column = 3)

oneButton.grid(row = 4, column = 0)
twoButton.grid(row = 4, column = 1)
threeButton.grid(row = 4, column = 2)
mullButton.grid(row = 4, column = 3)

zeroButton.grid(row = 5, column = 0)
pointButton.grid(row = 5, column = 1)
equalButton.grid(row = 5, column = 2)
divideButton.grid(row = 5, column = 3)

root.mainloop()