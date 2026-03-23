fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Displaying elements from last index to first index with their lengths:\n")
for fruit in fruits[::-1]:
    print("fruit:",fruit,"Length: ",len(fruit))
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.append(fruit[::-1])
print("\nOriginal List:")
print(fruits)
print("\nList with reversed elements:")
print(reversed_fruits)
