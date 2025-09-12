def get_input():
    return list(map(int,input("Enter the number:").split()))

def pos_neg(lst):
    positive=sum(1 for x in lst if x>0)
    negative=sum(1 for x in lst if x<0)
    zero=sum(1 for x in lst if x==0)
    return positive,negative,zero


def main():
    lst=get_input()

    pos,neg,zero=pos_neg(lst)

    print("The number of positive numbers is:",pos)
    print("The number of negative numbers is:",neg)
    print("The number of zero numbers is:",zero)
main()