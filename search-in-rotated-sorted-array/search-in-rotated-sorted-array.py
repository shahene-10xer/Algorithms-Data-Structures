class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        nums.sort()
        print(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return hashmap[nums[mid]]
            else:
                continue
            
        return -1 
                