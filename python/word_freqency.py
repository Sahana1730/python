import string

text = input("Enter text: ").lower()
for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
