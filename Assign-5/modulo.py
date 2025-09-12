def tuple_modulo(t1, t2):
    return tuple(a % b for a, b in zip(t1, t2))

# Example
tuple1 = (10, 20, 30)
tuple2 = (3, 7, 4)
mod_result = tuple_modulo(tuple1, tuple2)
print("Modulo Result:", mod_result)