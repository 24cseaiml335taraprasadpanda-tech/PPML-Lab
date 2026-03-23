p = float(input('Enter principal: '))
t = float(input('Enter time: '))
r = float(input('Enter rate of interest: '))
n = float(input('Enter number of times interest is compounded per year: '))

si = (p * t * r) / 100
ci = p * (1 + (r / (100 * n))) ** (n * t)   

print('Simple interest is: ', si)
print('Compound amount is: ', ci)
print('Compound interest is: ', ci - p)
