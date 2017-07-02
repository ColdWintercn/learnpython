class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = list(s)
        t1 = list(t)
        for i in s1:
            for j in range(0,len(t1)):
                if i == t1[j]:
                    t1.pop(j)
                    break
        return ''.join(t1)