# assignment-1
#write a function that takes two sentence
#split the words by space and create two lists of words.
# then it should generate a new list with elements that are common to both the lists.
# the new list should not have any duplicates and input lists may be of different lengths

a=input(("enter a sentence"))
b=input("enter an another sentence")
l1=a.split(" ")
print(l1)
l2=b.split(" ")
print(l2)
new_list=[]
for i in l1:
    for x in l2:
        if i==x:
            new_list.append(i)
print('duplicating words',new_list)
new_list1=[]
for k in l1:
    if k not in new_list:
        new_list1.append(k)
for r in l2:
    if r not in new_list:
        new_list1.append(r)
print('without duplicating words',new_list1)


# assignment-2
# create a class called calculator
# while creating object pass two numbers into it.
# when call object.add(),multiply(),divide()...toget
# result

class calculator():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print(self.x+self.y)
    def subtract(self):
        print(self.x-self.y)
    def divide(self):
        print(self.x/self.y)
    def multiply(self):
        print(self.x*self.y)
num=calculator(2,2)
num.add()
num.subtract()
num.divide()
num.multiply()
