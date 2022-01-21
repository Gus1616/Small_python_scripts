"""
Program that checks for a palindrome
Write an iterative version of an isPal function to check whether a supplied string is a palindrome.
initialise count to 0
iterate i through length of inputted string
check if first letter is == to last letter by slicing the string
if yes, print confirmation
if no, print no palindrome

"""


while True:
    string = input("Enter any word :")
    if string == '':
        print('you entered nothing!!')
        break
    else:

        i = 0
        for i in range(len(string)):
            if string[i] != string[-1-i]:

                print(string, 'you do not have a palindrome')
                break
            else:
                print(string,  'you have a palindrome')
                break

print('finito')