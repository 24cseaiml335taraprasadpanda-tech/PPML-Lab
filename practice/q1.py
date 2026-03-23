n=input("Enter a five digit number: ")
for i in range(len(n)):
    if (i+1)%2!=0:
        print(n[i],end="\t")