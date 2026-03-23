m = int(input("Enter starting number (m): "))
n = in
num_list = []
for i in range(m, n + 1):
    num_list.append(i)
print("\nList of natural numbers:")
print(num_list)
total = sum(num_list)
average = total / len(num_list)
largest = max(num_list)
smallest = min(num_list)
print("\nSum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
new_list = []
for num in num_list:
    if num % 3 != 0:
        new_list.append(num)
print("\nList excluding numbers divisible by 3:")
print(new_list)
