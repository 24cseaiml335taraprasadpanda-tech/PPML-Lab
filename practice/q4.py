n=input("Enter a String: ")
rev=n[::-1]
print("Reverse is :",rev)
vowel_count=0
consonant_count=0
for i in range(len(n)):
    if n[i] in "AEIOUaeiou":
        vowel_count+=1
    else:
        consonant_count+=1
print("Vowels count: ",vowel_count)
print("Consonant Count: ",consonant_count)