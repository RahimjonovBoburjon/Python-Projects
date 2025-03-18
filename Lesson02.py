def numbers(x,y,z):
    return x + y + z
print(numbers(7,8,9))

def numbers(x,y,z):
    return x - y - z
print(numbers(7,8,9))

def numbers(x,y,z):
    return x * y * z
print(numbers(7,8,9))

def numbers(x,y,z):
    return x / y / z
print(numbers(7,8,9))

# ----------------------

def ism(name):
    return f"Salom {name}"
name = input("Ismingizni kiriting: ")
print(ism(name))

# Masala-1:

def fullname(ism, familiya):
    return f"Salom {ism} {familiya}"

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")

print(fullname(ism, familiya))

# Masala-2:

def sonlar(*numbers):
    return sum(numbers)

print(sonlar(8, 10, 11))