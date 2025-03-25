# Task-1
telefon = input("Telefon raqamini kiriting: ")
raqamlar = {
    "0": "Nol",
    "1": "Bir",
    "2": "Ikki",
    "3": "Uch",
    "4": "To'rt",
    "5": "Besh",
    "6": "Olti",
    "7": "Yetti",
    "8": "Sakkiz",
    "9": "To'qqiz"
}
output = ""
for tel in telefon:
    output += raqamlar.get(
        tel, "+") + " "
print(output)

# Task-2
numbers = [1, 7, 10, 1, 3, 2, 5, 7, 0, -2, -25, 6]
uniques = []

for number in numbers:
    if number not in uniques and number % 2 == 0 and number > 0:
        uniques.append(number)
        uniques.sort()

print(uniques)

# Task-3
numbers = [1, 7, 10, 1, 3, 2, 5, 7, 0, -2, -25, 6, 4, 8, 17, 21, 23, 25]
uniques = []

for number in numbers:
    if number > 1:
        result = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                result = False
                break
        if result and number not in uniques:
            uniques.append(number)

uniques.sort()
print(uniques)