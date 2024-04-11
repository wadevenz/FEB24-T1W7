'''
take input of three numbers; a, b, c

If a > b
    if a > c
        display a
    else
        display c
else
    if b > c
        display b
    else
     display c
end
'''

a = int(input("Please input first number: "))
b = int(input("Please input second number: "))
c = int(input("Please input third number: "))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

# also 

if a > b and a > c:
    print (a)
elif b > c and b > a:
    print (b)
else:
    print (c)