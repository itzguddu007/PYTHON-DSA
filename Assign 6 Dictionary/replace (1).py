# Function to take replacement dictionary as input
def input_replacement_dict():
    repl_dict = {}
    n = int(input("Enter the number of words to replace: "))
    for i in range(n):
        key = input(f"Enter the word to replace ({i+1}): ")
        value = input(f"Enter the replacement for '{key}': ")
        repl_dict[key] = value
    return repl_dict

# Take the main string from user
test_str = input("Enter the original string: ")

# Take replacement dictionary from user
repl_dict = input_replacement_dict()

print("\nOriginal String:", test_str)
print("Replacement Dictionary:", repl_dict)

# Replace words
words = test_str.split()
result_words = [repl_dict.get(word, word) for word in words]
result_str = " ".join(result_words)

# Display result
print("\nReplaced String:", result_str)

