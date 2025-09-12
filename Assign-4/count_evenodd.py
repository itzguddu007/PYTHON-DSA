def get_input():
    return list(map(int,input("Enter the numbers: ").split()))

def count_odd_even(lst):
    even=sum(1 for x in lst if x%2==0 )
    odd=sum(1 for x in lst if x%2==1 )
    return even,odd

def main():
    lst=get_input()

    even,odd=count_odd_even(lst)   

    print("Even Numbers: ",even)
    print("Odd Numbers: ",odd)
main()


