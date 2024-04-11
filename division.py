''' 
Input numerator as n and denominator as d:

If d = 0 
    display "Denominator cannot be 0"

else
    q = n / d 
    display q
'''

n = int(input("Enter Numerator: "))
d = int(input("Enter Denominator: "))

if d == 0:
    print("Denominator cannot be equal to zero")
else:
    q = n / d
    print (q)

