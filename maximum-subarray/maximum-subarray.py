class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, max_sum = 0, float('-inf')
        # iterate through nums, if current_sum < 0, restart sum to 0, try and find max again
        # Kadane's Algorithm
        # [5,4,-1,7,8]
        '''
        [-2,1,-3,4,-1,2,1,-5,4]
        '''
        
        for right in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[right]
            max_sum = max(current_sum, max_sum)
        
        return max_sum