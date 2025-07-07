class Calculator:
    num=100  #class varibale

    def __init__(self, a, b):
        self.firstNum=a
        self.lastNum=b
        print("inside the constructor")

    def getData(self):
        print("Executing method in class")

    def summation(self):
        return self.firstNum + self.lastNum + Calculator.num

obj= Calculator(4,5)
obj.getData()
print(obj.summation())
print(obj.num)