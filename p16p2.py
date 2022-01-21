"""common divisors

define function with two arguments
have for loop that iterates i through 1 to the min of two entered numbers + 1
if i has no remainder in both numbers
loop is incremented
two variables for inputted numbers defined
if number is <= 0, print error
else
print function

"""


def find_divisors(num1, num2):
    """
    function calculates common divisors of two numbers
    """
    # empty tuple
    divisors = ()
    for i in range(1, min(num1, num2) +1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i, )
    return divisors


while True:
    number1 = int(input('enter a number greater than zero: '))
    number2 = int(input('enter another number greater than zero: '))

    if number1 <= 0 or number2 <= 0:
        print('I said the number should be greater than zero')
        break
    else:
        divisors = find_divisors(number1, number2)
        print('the common divisors of ', number1, 'and ', number2, 'are', divisors)

        total = 0
        for d in divisors:
            total += d
        print('sum of the common divisors is: ', total)

print('finished')