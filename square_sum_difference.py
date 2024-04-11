'''
intialise sum_of_squares = 0
initialise sum = 0
initialise 1 = 1

while i <= 100
    sum_of_squares = sum_of_squares + i * i
    sum = sum + i
    i = i + 1

    square_of_sum = sum * sum

    diff = square_of_sum - sum_of_squares

'''


sum_of_squares = 0
sum = 0
# i = 1

# while i <= 100:
#     sum_of_squares = sum_of_squares + i ** 2
#     sum = sum + i
#     i += 1

# square_of_sum = sum * sum

# diff = square_of_sum - sum_of_squares
# print (diff)


for i in range (1, 101):
    if i < 100:
        sum_of_squares += i * i
        sum += i
    else:
        square_of_sum = sum * sum


diff = square_of_sum - sum_of_squares
print(diff)
