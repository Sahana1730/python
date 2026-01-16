#append - Adds an item to the end of the list
my_list = [1, 2, 3] 
my_list.append(4)  # my_list is now [1, 2, 3, 4]
print(my_list)

#sort - Sorts the items of the list in ascending order
numbers = [5, 2, 9, 1]
numbers.sort()  # numbers is now [1, 2, 5, 9]
print(numbers)

#reverse - Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()  # fruits is now ['cherry', 'banana', 'apple']
print(fruits)

#insert - Inserts an item at a given position
a=['a', 'b', 'd']
a.insert(2,'c')  # a is now ['a', 'b', 'c', 'd']
print(a)

#pop - Removes and returns an item at a given position (default is the last item)
a=[1,2,3,4,5,6,7]
a.pop(0)
print(a)

#remove - Removes the first occurrence of a value
a=[1,2,3,4,5,6,7]
a.remove(5)
print(a)