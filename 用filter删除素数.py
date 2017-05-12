# python
i = range(101)
i.pop(0)
def is_prime_number(a) :
	judge = 2
	while a % judge != 0 and judge < a :		
		judge = judge + 1
	if judge == a :
		return False
	else :
		return True
print filter(is_prime_number,i)
