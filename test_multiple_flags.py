
"""Different ways to test multiple flags"""

x,y,z = 1,0,1

if x==1 or y==1 or z==1:
	print('passed')

if 1 in (x,y,z):
	print('passed')

#Test for truthness
if x or y or z:
	print ('passed')

if any((x,y,z)):
	print('passed')

if any(t > 0 for i in (x,y,z)):
	print('passed')