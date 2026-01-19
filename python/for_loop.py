# Simple for loop to print numbers from 1 to 5 (n-1)
for i in range(1,6):
    print(i)

for i in range(1,20,2):
    print(i)

#list iteration using for loop
l=[1,4,"sahana",6.5]
for i in l:
    print(i)


#for loop with else
for i in range(1,6):
    print(i)
else:
    print("loop is ended")


#break statement in for loop
for i in range(1,11):
    print(i)
    if i==5:
        break

#continue statement in for loop (skips the current iteration(5) and continues with the next iteration)
for i in range(1,11):
    if i==5:
        continue
    print(i)


#pass statement in for loop (does nothing, used as a placeholder)
for i in range(1,11):
    if i==5:
        pass
    print(i)