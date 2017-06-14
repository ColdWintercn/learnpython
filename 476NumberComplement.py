#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        two = []
        while True:
            if num != 0 :								
				two.append(str(num % 2))
				num = num / 2           
			else:
				break
        list = two[::-1]
        newlist = []
        for i in range(len(list)):
            if list[i] == '0':
                newlist.append('1')
            if list[i] == '1':
                newlist.append('0')
        sum = int(''.join(newlist),2)
        return sum







