a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
x=a
y=b
while y!=0:
    x,y=y,x%y
m=x
n=c
while n!=0:
    m,n=n,m%n
print("GCD is : ",m)