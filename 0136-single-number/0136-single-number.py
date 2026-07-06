class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)) :
            if nums.count(nums[i])==1 :
                return nums[i]