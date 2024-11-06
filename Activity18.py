#Write a program to understand how the operator precedence works

num = 18
num2 = 8
num3 = 9
num4 = 76
num5 = 189
num6 = 999
str = 'cat'

cal = (num*num2)+(num3/num4)**num5
print(cal)
if str == 'cat' or str == 'dog' and num>=1000:
    print('We are trying something')
else:
    print('See you again in the next class')