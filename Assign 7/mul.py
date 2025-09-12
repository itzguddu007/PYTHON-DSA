def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# --- User Input ---
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Multiplication of list is:", multiply_list(numbers))

     