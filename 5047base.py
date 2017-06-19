#python
class Solution(object):
    def convertToBase7(self, num):
        l = []
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        judge = 1
        if num < 0 :
            num = abs(num)
            judge = 0
        
        while num > 0:
            d = num % 7
            l.append(str(d))
            num = num / 7
        
        if judge == 0:
            l.append('-')
        s = l[::-1]
        p = ''.join(s)
        
        return p