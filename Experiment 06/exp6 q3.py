sentence = input("Enter a sentence: ")
list1 = sentence.split()
print("\nElements of list1 with index:")
for index, word in enumerate(list1):
    print(index, word)
list2 = []
n = len(list1)
for i in range(1, n + 1):
    list2.append(i)
list3 = list(zip(list1, list2))
print("\nCombined list (list3):")
print(list3)
