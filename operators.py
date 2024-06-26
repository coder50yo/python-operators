#!/usr/bin/env python3

# operators.py

def demonstrate_operators():
    # Arithmetic Operators
    a = 10
    b = 3
    print(f"Arithmetic Operators:")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a // b = {a // b}")
    print(f"a % b = {a % b}")
    print(f"a ** b = {a ** b}\n")

    # Comparison Operators
    x = 5
    y = 10
    print(f"Comparison Operators:")
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print(f"x > y: {x > y}")
    print(f"x < y: {x < y}")
    print(f"x >= y: {x >= y}")
    print(f"x <= y: {x <= y}\n")

    # Logical Operators
    p = True
    q = False
    print(f"Logical Operators:")
    print(f"p and q: {p and q}")
    print(f"p or q: {p or q}")
    print(f"not p: {not p}\n")

    # Bitwise Operators
    m = 10
    n = 4
    print(f"Bitwise Operators:")
    print(f"m & n: {m & n}")
    print(f"m | n: {m | n}")
    print(f"m ^ n: {m ^ n}")
    print(f"~m: {~m}")
    print(f"m << 2: {m << 2}")
    print(f"m >> 2: {m >> 2}\n")

    # Assignment Operators
    c = 5
    print(f"Assignment Operators:")
    c += 2
    print(f"c += 2: {c}")
    c -= 2
    print(f"c -= 2: {c}")
    c *= 2
    print(f"c *= 2: {c}")
    c /= 2
    print(f"c /= 2: {c}")
    c //= 2
    print(f"c //= 2: {c}")
    c %= 3
    print(f"c %= 3: {c}")
    c **= 2
    print(f"c **= 2: {c}\n")

    # Identity Operators
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"Identity Operators:")
    print(f"list1 is list2: {list1 is list2}")
    print(f"list1 is not list2: {list1 is not list2}")

if __name__ == "__main__":
    demonstrate_operators()
