#using function recursion of sum of n natural numbers
n=0
def sum(n):
    
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
n=int(input("enter a number:"))
sum=sum(n)    
print(f"the sum is :{sum}")


def pattern(n):
    if n == 0:
        return
    print('*' * n)
    pattern(n - 1)
n = int(input("Enter the number of rows: "))
pattern(n)            #output for n=5
# *****
# ****
# ***
# **
# *

