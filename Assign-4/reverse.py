def get_input():
    return list(map(int,input("Enter the numbers: ").split()))

# def get_reverse(lst):
#     return lst[::-1]

# def main():
#     lst=get_input()
#     result=get_reverse(lst) 
#     print("The list after reversing is:",result)
# main()
lst=get_input()
result=lst[::-1]
print("reverse: ",result)