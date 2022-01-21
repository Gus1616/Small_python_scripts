"""Two suggested optimisations for the algorithm to calculate the divisors of a number are to initalise the divisors
tuple to include 1 and the number itself and to only search from 2 and as far as half of the number. Revise
the solution on Pages 14–17 of the slides to include these optimisations.

define function
within function
have tuple to take divisors, include 1 and num1 (inputted number
check for divisors with for loop, iterate through from 2 to num1//2 + 1
if num1 % i == 0, increment loop
return the divisors
have variable for inputted number
if number <= 0, print error
else: print function



"""


def find_divisors(num1):
    """
    efficient function that calculates the divisors of a number
    """

    divisors = (1, num1)
    for i in range(2, num1//2 + 1):
        if num1 % i == 0:
            divisors += i,

    return divisors


number1 = int(input('enter a number greater than zero: '))


if number1 <= 0:
    print('I said the number should be greater than zero')
else:
    divisors = find_divisors(number1)
    print('the divisors of ', number1, 'are', divisors)

    total = 0
    for d in divisors:
        total += d
    print('sum of the divisors is: ', total)

print('finished')