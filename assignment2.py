# given a list L and an interger n,rotate L to the right by n places
#if n is negative rotate L to the left by n places
#example
#L=[1,2,3,4,5,6,7,8,9,10]
#if n is 3 then L=[8,9,10,1,2,3,4,5,6,7]
#if n is -3 then L=[4,5,6,7,8,9,10,1,2,3]

#with function

def rotate(L,n):
    if n==0:
        return
    if n>0:
        for i in range(n):
            x=L.pop()
            L.insert(0,x)
    else:
        for i in range(-n):
            x=L.pop(0)
            L.append(x)
L=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter an integer"))
rotate(L,n)
print(L)

#withoput function #uses slicing in it
myList =[5, 20, 34, 67, 89, 94, 98, 110]
print("List before rotation = ",myList)
n=int(input("input an number"))
# Rotating the List
myList=(myList[-n:]+myList[:-n])
print("Updated List after rotation = ",myList)



# Assignment-2------Using function
# fibonacci sequence is 1,1,2,3,5,8,13,21...
#given a n ,write a function to return n numbers of fibonacci sequence

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n=int(input("enter an integer"))
for i in range(n+1):
    print(Fibonacci(i))


#Assignment-3------Using function
#write a function to check whether it is palindrome

def is_palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
n=input("enter an string")
print(is_palindrome(n))



