def si(p,t,r):
    return (p*t*r)/100
p=float(input("Enter principal Amount"))
r=float(input("Enter rate of intrest"))
t=float(input("Enter time in years"))
print("Simple intrest is",si(p,t,r))