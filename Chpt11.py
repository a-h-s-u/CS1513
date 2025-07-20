#####################################
## Alice Hsu
## Chapter 10/11/12: Programming Exercise
## HW Pg 634: #4, 6, 7
#####################################


## Largest List Item
def largest(n):
    if len(n)==1:
        return n[0]
    rest=largest(n[1:])
    if n[0]>rest:
        return n[0]
    else:
        return rest
items=input("Enter a list of items separated by spaces: ")
print("Largest item:",largest(items))

## Sum of Numbers
def sum_num(n):
    if n==1:
        return 1
    rest=sum_num(n-1)
    return n+rest
num=int(input("Enter a number: "))
print("Sum:",sum_num(num))

## Recursive Power Method
def power(x,y):
    if y==0:
        return 1
    rest=power(x,y-1)
    return x*rest
num=int(input("Enter number to be raised: "))
exponent=int(input("Enter the exponent: "))
print("The number is equal to:",power(num,exponent))
