class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.
        
        Write brute force solution (O(m + n))
        then watch neetcode 3/28/23 and write optimized 2 heap solution
        '''
        
        '''
        brute force:
        1) merge both arrays into one array
        2) use two ptrs to make them sorted
        3) if odd: eturn mid, if even: return average of left mid and right mid
        '''
        merged_arr = []
        num1_ = num2_ = 0
        while num1_ < len(nums1) and num2_ < len(nums2):
            if nums1[num1_] < nums2[num2_]:
                merged_arr.append(nums1[num1_])
                num1_ += 1
            else:
                merged_arr.append(nums2[num2_])
                num2_ += 1
        
        if num1_ < len(nums1) :
            merged_arr = merged_arr + nums1[num1_:]
        if num2_ < len(nums2):
            merged_arr = merged_arr + nums2[num2_:]
        
        mid = len(merged_arr) // 2
        if len(merged_arr) % 2 != 0:
            return float(merged_arr[mid])
        else:
            print(merged_arr)
            print(merged_arr[mid], merged_arr[mid-1])
            return (merged_arr[mid] + merged_arr[mid - 1]) / 2
        