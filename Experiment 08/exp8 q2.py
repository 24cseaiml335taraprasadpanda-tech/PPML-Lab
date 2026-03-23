def cheak(a):
    return "Even" if a%2==0 else "Odd"
n=int(input("Enter a number: "))
print(f"{n} is {cheak(n)}")