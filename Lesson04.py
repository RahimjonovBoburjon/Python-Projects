# Task-1:
numbers=[0,3,5,15,45,77,90]
new=[]
new.append(min(numbers))
print(new)

# Task-2:
numbers=[0,3,5,15,45,77,90]
min1 = numbers.index(min(numbers))
max1 = numbers.index(max(numbers))
numbers[min1], numbers[max1] = numbers[max1], numbers[min1]
print(numbers)