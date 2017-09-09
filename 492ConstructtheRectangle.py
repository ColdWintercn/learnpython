class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]       
        """
        import math
        j = 1
        i = int(math.sqrt(area))
        while i <= area:
            j = area / i
            if i*j == area:
                break
            i += 1
        if i < j:
            temp = i
            i = j           
            j = temp
        return [i,j]