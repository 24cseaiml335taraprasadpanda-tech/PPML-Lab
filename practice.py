# n="tara prasad panda"
# vowel=0
# consonant=0
# for i,ch in enumerate(n,start=6):
#     if ch==" ":
#         continue
#     elif ch in "AEIOUaeiou":
#        vowel+=1
#     else:
#         consonant+=1
# print(vowel)
# print(consonant)
# def square(a):
#     return a*a
# n=int(input("Enter a number: "))
# print(f"square of {n} is {square(n)}")
# def cheak(a):
#     return "even" if a%2==0 else "odd"
# n=int(input("Enter a number: "))
# print(f"{n} is {cheak(n)}")
# def fact(a):
#     if a<0:
#         print("factorial of negetive numbers can not be found")
#         exit
#     else:
#         return 1 if a==1 or a==0 else a*fact(a-1)
# n=int(input("Enter a number: "))
# print(f"factorial of {n} is {fact(n)}")
# def primecheak(a):
#     if a<2:
#         return "cant be defined"
#     for i in range(2,a):
#         if a%i==0:
#             return "not prime"
#     return "prime"
# n=int(input("Enter a number: "))
# print(f"{n} is {primecheak(n)}")
# def rev(a):
#     return a[::-1]
# n=input("Enter a string: ")
# print(f"reverse is {rev(n)}")
# def rev(s):
#     return s if s=="" else rev(s[1:])+s[0]
# n=input("Enter a string: ")
# print(f"reverse is {rev(n)}")
a="tara"
print(a*3,end=" ")