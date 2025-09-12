# Get dictionary from user
n = int(input("How many items in the dictionary? "))
d = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

# Sort by key
sorted_by_key = dict(sorted(d.items()))
print("Sorted by key:", sorted_by_key)

# Sort by value
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print("Sorted by value:", sorted_by_value)

