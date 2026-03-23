n=int(input("Enter a number: "))
n1=n
rev=0
while(n!=0):
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
if n1==rev:
    print(n1," is palindrome.")
else:
    print(n1," is not palindrome.")
