#Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?

sp1 = 10
sp2 = 20
sp3 = 30
ave = (sp1+sp2+sp3)/3
print(ave)

if sp1<ave:
   print('The',sp1,'is slower than the average speed of all  cyclists by',ave-sp1,' by that much speed in kilometres exactly.')
if sp2<=ave:
   print('The',sp2,'is travelling at the average speed.')
if sp3>ave:
   print('The',sp3,'is faster than the average speed of all  cyclists by',sp3-ave,' by that much speed in kilometres exactly.')