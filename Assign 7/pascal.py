def generate_row(prev_row):
    """Generate the next row of Pascal's Triangle from the previous row"""
    new_row = [1]
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i+1])
    new_row.append(1)
    return new_row

def pascal_triangle(n):
    row = [1]  # start with the first row
    for _ in range(n):
        print(" ".join(map(str, row)))
        row = generate_row(row)  # generate next row

# --- User Input ---
n = int(input("Enter number of rows for Pascal's Triangle: "))
pascal_triangle(n)