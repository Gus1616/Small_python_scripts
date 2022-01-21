"""
Write a program that takes a page (eg the source of a Web page that you have saved), counts
the occurrences of left angle brackets (<), right angle brackets (>), newlines, the lowercase
letter e, the string <!-- and the string --> and prints out the results to a file results.txt.
Your program should make appropriate checks regarding the existence of the input and output
files.

open and read file
assign variable to reading file
open new file to write
count each object in read file
write results in new file
open new file
print results



"""

f = open("readexample.txt", "r")
x = (f.read())
b = open("write_example.txt", "w")
vowels = 'a, e, i, o, u'
count1 = x.count(vowels)
count2 = x.count('>')
count3 = x.count('e')
count4 = x.count('<!--')
count5 = x.count(' -->')
count6 = x.count('\n')

b.write(str(count1) + '\n')
b.write(str(count2) + '\n')
b.write(str(count3) + '\n')
b.write(str(count4) + '\n')
b.write(str(count5) + '\n')
b.write(str(count6) + '\n')

b.close()

fh1 = open("write_example.txt", 'r')
print(fh1.read())



