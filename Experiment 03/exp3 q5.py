a=int(input("Enter the first subject mark is :"))
b=int(input("Enter the second subject mark is :"))
c=int(input("Enter the third subject mark is :"))
d=int(input("Enter the fourth subject mark is :"))
e=int(input("Enter the fiveth subject mark is :"))

sum=a+b+c+d+e
per=(sum/250)*100
print("The percentage is ",per)
if(per>=90 and per<=100):
    print("it is O grade")
elif(per>=80 and per<=90):
   print("it is E grade")
elif(per>=70 and per<=80):
   print("it is A grade")
elif(per>=50 and per<=60):
   print("it is C grade")
elif(per>=0 and per<=50):
   print("it is F grade")
else:
   print("other are a not included")