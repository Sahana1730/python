a=(input("enter your name:"))
print(f"good afternoon {a}")

letter='''Dear <|NAME|>,
              You are selected!
              Date: <|DATE|>'''

print(letter.replace("<|NAME|>","sahana").replace("<|DATE|>","20th june 2024"))

#detect double space in string
string="i am  sahana"
print(string.find("  "))
#output -1 if no space found and other index if found

#replace double space with single space
string=string.replace("  "," ")
print(string)

#escape sequence
a="Sahana is very good girl.\nshe is also a best student."
print(a)

