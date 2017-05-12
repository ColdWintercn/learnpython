#python
# -*- coding: utf-8 -*-
print u'哈哈哈'
def Fibonacci ( a ) :
	if a <= 1 :
		return a
	else :
		return Fibonacci( a - 1 ) + Fibonacci ( a - 2 )
a = int(raw_input ( '请输入一个整数：'.decode('utf-8').encode('gbk') ))
print Fibonacci( a )		
