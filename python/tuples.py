#tuple are immutable sequences, typically used to store collections of heterogeneous data.
#tuples are written in round brackets ()
a = (1, 2, 3, "hello", 4.5, True)
print(a)

#methods in tuple
#count() - returns the number of occurrences of a specified value
t = (1, 2, 3, 2, 4, 2)
count = t.count(2)
print(count)

#index() - returns the index of the first occurrence of a specified value
index = t.index(3)
print(index)