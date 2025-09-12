def take_input():
    """Take user inputs and return as a list of integers"""
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    return nums

def separate_odd_even(nums):
    """Return even and odd lists"""
    even = [n for n in nums if n % 2 == 0]
    odd = [n for n in nums if n % 2 != 0]
    return even, odd

def display_list(lst,name):
    """Display list elements"""
    if lst:
        print(f"{name} numbers:", lst)
    else:
        print(f"No {name} numbers found!")

def subtract_lists(list1, list2):
    """Subtracts element-wise, fills empty places with '0' (string)"""
    max_len = max(len(list1), len(list2))
    result = []
    for i in range(max_len):
        if i < len(list1) and i < len(list2):
            result.append(list1[i] - list2[i])
        else:
            result.append("0")  # fill empty space with string "0"
    return result

# Main Program
def main():
    nums = []
    even = []
    odd = []
    odd_minus_even = []
    even_minus_odd = []

    while True:
        print("\n---- MENU ----")
        print("1. Take user input and separate odd-even")
        print("2. Display even numbers")
        print("3. Display odd numbers")
        print("4. Store Odd - Even in another list")
        print("5. Show Odd - Even list")
        print("6. Store Even - Odd in another list")
        print("7. Show Even - Odd list")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            nums = take_input()
            even, odd = separate_odd_even(nums)
            print("Numbers stored successfully!")

        elif choice == "2":
            display_list(even, "Even")

        elif choice == "3":
            display_list(odd, "Odd")

        elif choice == "4":
            odd_minus_even = subtract_lists(odd, even)
            print("Odd - Even list created!")

        elif choice == "5":
            display_list(odd_minus_even, "Odd - Even")

        elif choice == "6":
            even_minus_odd = subtract_lists(even, odd)
            print("Even - Odd list created!")

        elif choice == "7":
            display_list(even_minus_odd, "Even - Odd")

        elif choice == "8":
            print("Exiting program... Bye!")
            break

        else:
            print("Invalid choice! Try again.")

# Run program
if __name__ == "__main__":
    main()