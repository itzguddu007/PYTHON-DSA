def tup_copy(source_tup,indices):
    return tuple(source_tup[i] for i in indices if 0<=i<len(source_tup))

get_input=input("Enter the main tuple: ")
source_tup=tuple(map(int,get_input.split()))

indices_str=input("Enter the indieces: ")
indices=list(map(int,indices_str.split()))

new_tuple=tup_copy(source_tup,indices)

print("New Tuple is: ",new_tuple)