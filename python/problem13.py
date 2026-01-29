n=int(input("enter:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i)



n = int(input("Enter a number: "))
count = 0
if n == 0:
    count = 1
else:
    while n != 0:
        n //= 10
        count += 1

print("Number of digits:", count)


#reverse a number without string method:
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed number:", rev)
