dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print(merged_dict)



data = {'a': 3, 'b': 1, 'c': 2}

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_dict)



data = {'a': 3, 'b': 1, 'c': 2}

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)
