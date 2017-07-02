class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        list1 = []
        s = set(list1)
        for i in nums:
            count += 1
            s.add(count)

        s1 = set(nums)
        
        for i in s1:
            s.remove(i)
        list2 = list(s)
        return list2