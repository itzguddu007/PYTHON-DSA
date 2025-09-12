def get_input():
    return list(map(int, input("Enter the numbers with spaces: ").split()))



def rev(lst):
    if len(lst)>=2:
        lst[0],lst[-1]=lst[-1],lst[0]
    return lst

def main():
    lst=get_input()
    result=rev(lst)
    print("List after swapping the first and last  entered list is:",result)
main()

