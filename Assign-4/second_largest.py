def get_input():
    return list(map(int,input("Enter the Numbers: ").split()))

def second_largest(lst):
    unique=list(set(lst))

    if len(unique)<2:
        return None
    unique.sort()
    return unique[-2]

def main():
    lst=get_input()
    result=second_largest(lst)
    print("The Second Largest Element is: ",result)
main()
