# Dictionary in Python
#written in flower braces {}
#key-value pairs

my_dict = {
    "name": "Alice",  
    "age": 30,       
    "city": "New York"  
}
print(my_dict["name"])

#methods in dictionary
my_dict = {
    "name": "Alice",  
    "age": 30,       
    "city": "New York"  
}
print(my_dict.get("age"))
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_dict.update({"age":35, "dob":"aug 17"})
print(my_dict)

