class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        notebook = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in notebook:
                return [notebook[complement], i]
                
            notebook[num] = i
            
        return []
        
