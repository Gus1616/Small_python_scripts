"""
define function
set base case to 0 and 1, return 13 and 8 respectively
else
return formula set out
include print statement to show progress to base case
set while True block to repeatedly ask user for integer
assign variable n to user inputted integer
if negative print error and brake loop
else
call function
set for loop that iterates through range(0, number + 1)
print the function result


"""


def function(n):
    """ a function that returns f(n - 2) + (13 * (f(n - 1)))  """
    if n == 0:
        return 13
    elif n == 1:
        return 8

    else:
        print('heading to the base', n)
        return function(n - 2) + (13 * (function(n - 1)))


while True:
    n = int(input('enter a number greater than 0 and I will find the series: '))
    if n <= 0:
        print('I said add a number greater than zero!')
        break

    else:
        for i in range(n+1):
            print(function(i))