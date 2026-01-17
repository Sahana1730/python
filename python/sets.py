#sets are written in curly braces {}
#sets do not allow duplicate values
my_set = {1,2,3,4,5,5,5}
print(my_set)

#to write epmty set
s=set()
print(type(s))

#methods in set
#add() - adds an element to the set
my_set.add(6)
print(my_set)

#remove() - removes a specified element from the set
my_set.remove(3)
print(my_set)

#clear() - removes all elements from the set
my_set.clear()  
print(my_set)

#union() - returns a set that is the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)
#intersection() - returns a set that is the intersection of two sets
set4 = set1.intersection(set2)  
print(set4)
#difference() - returns a set that contains the difference between two sets
set5 = set1.difference(set2)  
print(set5)
#symmetric_difference() - returns a set that contains the symmetric difference between two sets
set6 = set1.symmetric_difference(set2)
print(set6)
#pop() - removes and returns an arbitrary element from the set
element = set1.pop()
print(element)
print(set1)
#len() - returns the number of elements in the set
length = len(set2)
print(length)