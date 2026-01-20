a=0
b=0
c=0
def num(a,b,c):
    a=int(input(f"enter a number:"))
    b=int(input(f"enter a number:"))
    c=int(input(f"enter a number:"))
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

result = num(a,b,c)
print(f"The greatest number is {result}")