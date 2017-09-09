class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= len(s):
            return ''.join(list(s)[::-1])
        if k < len(s) :
            if 2*k > len(s):
                l = []
                for i in range(k):
                    l.append(s[i])
                return ''.join(l[::-1])+''.join(list(s)[k:])
            else:
                for i in range(len(s)//k):
                    if i%2 == 0:
                        l = []
                        for j in range(k):
                            l.append(s[i*k+j])
                        if i != 0:
                            s = ''.join((list(s))[:i*k])+''.join(l[::-1])+''.join((list(s))[(i+1)*k:])
                        else :
                            s = ''.join(l[::-1]) + ''.join(list(s)[k:])
                if len(s)%k != 0 and (len(s)//k) %2 ==0:
                    l = []
                    for i in range(((len(s)//k)*k),len(s)):
                        l.append(s[i])
                    s = ''.join(list(s)[:(len(s)//k)*k])+''.join(l[::-1])
                return s 