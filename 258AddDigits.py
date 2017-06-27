class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """               
        while(True):    
            if num < 10 :
                break
            l = list(str(num))
            l2 = []
            for i in l:
                l2.append(int(i))
            num = 0
            for i in l2:
                num += i
            
        return num   
        