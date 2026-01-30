s = input("Enter a string: ")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)



data = {
    'a': 10,
    'b': 25,
    'c': 15
}

max_key = max(data, key=data.get)
print("Key with maximum value:", max_key)
