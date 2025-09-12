def make_sum(*args):
    print("Sum is:", sum(args))

# --- User Input ---
nums = list(map(int, input("Enter integers separated by space: ").split()))
make_sum(*nums)
