sonlar = [7, 15, 1, 98, 3]

sonlar.append(200)
# append bu - arrayga oxiriga qo'shadi

sonlar.insert(0, 100)
# insert bu - index kiritib son qo'shamiz. Masalan boshiga

sonlar.sort()
# sort bu - ketma ketlik bilan tartibga qo'yadi

sonlar.reverse()
# reverse bu - teskari yozib beradi

sonlar.pop()
# pop bu - oxirgi arrayni ob tashidi

print(7 in sonlar)
# ushbu sonlarda mavjudligini tekshiradi

print(sonlar.count(3))
# nechta borligini aytadi

print(sonlar)

# MASALA:

num = []

one = int(input("1 chi son kiriting: "))
num.append(one)
two = int(input("2 chi son kiriting: "))
num.append(two)
three = int(input("3 chi son kiriting: "))
num.append(three)
four = int(input("4 chi son kiriting: "))
num.append(four)

num.insert(0, 1)
num.sort()
num.pop()
num.reverse()
print(num)