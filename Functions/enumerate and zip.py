fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwo"]

size = [5, 5, 6, 6, 9, 10, 5, 4]

for fruit in enumerate(fruits, start=1):
    print(fruit)


# zip function

print(dict(zip(fruits, size)))
print(list(zip(fruits, size)))