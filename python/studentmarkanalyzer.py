marks = list(map(int, input("Enter marks: ").split()))

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Grade:", grade)
