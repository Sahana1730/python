#slicing
name="sahana"
nameshort=name[0:3]#start from index 0 to index 2 excluding index 3
print(nameshort)
character=name[2]#accessing character at index 2
print(character)


#negative indexing
name="sahana"
print(name[-4 : -1])
print(name[2:5])


#slicing with skip index
a="0123456789"
print(a[1:7:3])#start from index 1 to index 6 excluding index 7 with a skip of 2

b="0123456789"
print(b[1:9:2])#start from index 1 to index 8 excluding index 9 with a skip of 2