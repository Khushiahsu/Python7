#Write to check a number is divisible by another number.

fra = int(input('Enter the numerators value please:'))
dec = int(input('Enter the denominators value please:'))
if fra%dec == 0:
    print('\n'+ str(fra) + ' is divisible by ' + str(dec))#concatenation
else:
    print('\n'+ str(fra) + ' is not divisible by ' + str(dec))#concatenation