class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            target = -nums[i]
            self.find_pair(nums, target, triplets, left)
        return triplets
        
    def find_pair(self, nums, target, triplets, left):
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                triplets.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total > target:
                right -= 1
            else:
                left += 1
        