num=int(input("Enter a number: "))
i=1 
count=0
while(i<=num):
    if(num%i==0):
        count+=1
    i+=1
if(count==2):
    print("The number is prime")
else:
    print("the number is not prime")