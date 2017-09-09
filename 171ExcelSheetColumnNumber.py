class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        l = list(s)
        l1 = list(reversed(l))
        for i in range(len(l)):
            if i == 0:
                sum += (ord(l1[i])-64)
            else:
                sum += 26**i*(ord(l1[i])-64)
        return sum