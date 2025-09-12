# Function to take dictionary input from user
def input_dictionary(dict_number):
    d = {}
    n = int(input(f"Enter the number of elements for Dictionary {dict_number}: "))
    for i in range(n):
        key = input(f"Enter key {i+1}: ")
        value = input(f"Enter value for '{key}': ")
        d[key] = value
    return d

# Input both dictionaries
print("Enter details for Dictionary 1:")
dict1 = input_dictionary(1)

print("\nEnter details for Dictionary 2:")
dict2 = input_dictionary(2)

# Display both dictionaries
print("\nDictionary 1:", dict1)
print("Dictionary 2:", dict2)

# Take key from Dict1 and search in Dict2
key_to_find = input("\nEnter a key to search (from Dictionary 1): ")

if key_to_find in dict1:
    if key_to_find in dict2:
        print(f"Key '{key_to_find}' found in Dictionary 2 with value: {dict2[key_to_find]}")
    else:
        print(f"Key '{key_to_find}' NOT found in Dictionary 2.")
else:
    print(f"Key '{key_to_find}' does not exist in Dictionary 1.")

# Merge two dictionaries
merged_dict = dict1.copy()
merged_dict.update(dict2)
print("\nMerged Dictionary:", merged_dict)

