class Solution:
    '''
    start from i and move out
    edge case when s is even, have i start at i + 1
    move outwards (l -= 1, r += 1)
    update res and res_len if current length > max_res
    2 while loops for even and odd
    doing same thing except even would start at i + 1 (no char in the middle)
    can have even palindrome inside of odd length string so make sure checking
    even is within the outer for loop
    runs O(n ^ 2) if you don't count updating res string
    
    '''
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                
                l -= 1
                r += 1
        # even length 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
            
                l -= 1
                r += 1
        
        return res