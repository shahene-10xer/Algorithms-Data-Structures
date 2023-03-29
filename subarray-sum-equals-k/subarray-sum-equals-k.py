class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = res = 0
        prefix_sums = { 0: 1 }
        
        for n in nums:
            cur_sum += n
            res += prefix_sums.get(cur_sum - k, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)
        
        return res