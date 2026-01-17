# words={
#     "madad":"help",
#     "dost":"friend",    
#     "pyaar":"love",

# }
# word=input("enter the word:")
# print(words[word])


# s=set()
# n=int(input("enter a number:"))
# s.add(int(n))
# n=int(input("enter a number:"))
# s.add(int(n))
# n=int(input("enter a number:"))
# s.add(int(n))
# n=int(input("enter a number:"))
# s.add(int(n))
# n=int(input("enter a number:"))
# s.add(int(n))
# n=int(input("enter a number:"))
# s.add(int(n))
# print(s)

s=set()
s.add(17)
s.add("17")
print(s)


s=set()
s.add(20)
s.add(20.0)
s.add("20")
s=len(s)
print(s)

d={}

name=input("enter name:")
lang=input("enter language:")
d.update({name:lang})
name=input("enter name:")
lang=input("enter language:")
d.update({name:lang})
name=input("enter name:")
lang=input("enter language:")
d.update({name:lang})
name=input("enter name:")
lang=input("enter language:")
d.update({name:lang})

print(d)