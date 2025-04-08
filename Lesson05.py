# Nechta so'z borligini aniqlab beradi:
s = input("Gap kiriting: ")
words = s.split()
print(len(words), "ta so'z")

# Unli va undoshlarni sanab beradi:
s = input("So'z kiriting: ")

words = s.split()
count = 0
count1 = 0

for c in s:
    if c != " ":
        if c.lower() in 'aoiue':
            count += 1
        else:
            count1 += 1

print("Unlilar soni:",count)
print("Undoshlar soni:",count1)