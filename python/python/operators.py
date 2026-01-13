#operators
#1. arithmetic operators (+, -, *, /, %, //, **)
#2. assignment operators (=, +=, -=, *=, /=, %=, //=, **=)
#3. comparison operators (==, !=, >, <, >=, <=)
#4. logical operators (and, or, not)
#5. bitwise operators (&, |, ^, ~, <<, >>)

a=17
b=30
c=a+b
print(c)

a=4-2 #assign 4-2 in a
print(a)
b=6
b+=4 #increment b by 4 (b=b+4)
b-=2 #decrement b by 2 (b=b-2)
b*=3 #multiply b by 3 (b=b*3)
b//=2 #floor divide b by 2 (b=b//2)
print(b)

#comparison operators
x=10
y=20
print(x==y) #equal to
print(x!=y) #not equal to  
print(x>y)  #greater than
print(x<y)  #less than  

#logical operators
p=True
q=False 
print(p and q) #logical and (both true)
print(p or q)  #logical or (at least one true)
print(not p)   #logical not (inverts value)
#bitwise operators
m=5  #binary: 0101
n=3  #binary: 0011
print(m & n)  #bitwise and: 0001 (1 in decimal)