##!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        a = []
        l = s.split()
        for i in l:
            a.append(i[::-1])
        str = ' '.join(a)
        return str
        