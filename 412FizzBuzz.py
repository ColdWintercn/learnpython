#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def fizzBuzz(self, n):
        d = []
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1
        while i <= n:
            
            if i%3 == 0 and i%5 == 0 :
                d.append('FizzBuzz') 
            elif i%3 == 0 :
                d.append('Fizz') 
            elif i%5 == 0 :
                d.append('Buzz') 
            else :
                d.append(str(i)) 
            i += 1
        return d
