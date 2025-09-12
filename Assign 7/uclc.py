def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("No. of Upper case characters:", upper)
    print("No. of Lower case characters:", lower)

# --- User Input ---
s = input("Enter a string: ")
count_case(s)
