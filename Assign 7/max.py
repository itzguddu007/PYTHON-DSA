def max_of_three(a, b, c):
    return max(a, b, c)

# --- User Input ---
a, b, c = map(int, input("Enter three numbers separated by space: ").split())
print("Max is:", max_of_three(a, b, c))
