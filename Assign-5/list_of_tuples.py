def cube_tuples(numbers):
    return [(n, n ** 3) for n in numbers]

# Example
list_input=input("Enter the elements: ")
lst=list(map(int,list_input.split()))
cubes = cube_tuples(lst)
print("Number-Cube Tuples:", cubes)