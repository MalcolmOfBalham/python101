def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"multiplying {a} x {b}")
    return a * b

def divide(a,b):
    print(f"dividing {a} / {b}")
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print(f" Age: {age}\n Height: {height}\n Weight: {weight}\n iq: {iq}")
