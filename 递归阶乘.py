# python

a = 10
def fbnq ( a ):
	if ( a == 1 ) :
		return 1
	else :
		return (a * fbnq ( a-1 ))
print fbnq (a)