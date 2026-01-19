#multipication of 2 using for loop
n=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} x {i}={n*i}")


#get a person name stored in list l 
l=["sahana","sanni","bharath","shaila","raju"]
for i in l:
    if(i.startswith('s')):
        print("letter starts with s:",i)


n=int(input("Enter a number: "))
i=1
while i <11:
    print(f"{n} x {i}={n*i}")
    i+=1

#prime number
num=int(input("Enter a number: "))
for i in range(2,num):
    if(num%i==0):
        print("not a prime number")
        break
else:
    print("prime number")


n=int(input("enter a number:"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1    
print("sum is:",sum)


#factorial of a number using for loop
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial is:",fact)

#star pattern
for i in range(1,6,2):
    for j in range(1,i+1):
        print("*",end="")
    print("")