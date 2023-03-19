from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Monotonically Decreasing Queue (if element being added is > max element (queue[0]), 
        popleft from queue) if element added is <, append to queue
        '''
        queue = deque()
        left, right = 0, 0
        output = []
        
        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            if left > queue[0]:
                queue.popleft()
            
            if right + 1 >= k:
                output.append(nums[queue[0]])
                left += 1
                
            right += 1
        
        return output
        