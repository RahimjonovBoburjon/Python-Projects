# 1-misol: Berilgan 2 sonning yig‘indisini hisoblash:
number1 = float(input("Birinchi sonni kiriting: "))
number2 = float(input("Ikkinchi sonni kiriting: "))

solve = number1 + number2
print("Yig‘indi:", solve)

# 2-misol: Berilgan son juft yoki toq ekanligini aniqlash:
number = int(input("Sonni kiriting: "))

if number % 2 == 0:
    print("Son juft!")
else:
    print("Son toq!")

# 3-misol: Foydalanuvchining tug‘ilgan yilidan yoshini va asrini aniqlash:
born = int(input("Tug‘ilgan yilingizni kiriting: "))
now = 2025

age = now - born
century = (born // 100) + 1

print("Sizning yoshingiz: ", age)
print("Tug‘ilgan asringiz: ", century)

# 4-misol: Berilgan hafta kunining nomini chiqarish:
day = int(input("Hafta kunining tartib raqamini kiriting: "))

if day == 1:
    print("Dushanba")
elif day == 2:
    print("Seshanba")
elif day == 3:
    print("Chorshanba")
elif day == 4:
    print("Payshanba")
elif day == 5:
    print("Juma")
elif day == 6:
    print("Shanba")
elif day == 7:
    print("Yakshanba")
else:
    print("Xatolik! Noto‘g‘ri hafta kuni!")