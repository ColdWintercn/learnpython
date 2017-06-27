class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        delete = []
        for i in range(len(nums)):
            if nums[i] == 0:
                delete.append(i)
                nums.append(0)
        for i in (delete[::-1]):
            nums.pop(i)
        