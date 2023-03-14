class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        
        hashmap = {}
        sliding window, start at left = 0, and iterate with right pointer
        
        if char doesn't exist in hashmap add it with its ith pointer
        save maximum length
        
        if it does exist, we have a repeating character, therefore substring is not valid
        we delete char starting from left until left == ith_repeating_char, decrement i
        
        keep going until the end 
        '''
        # dvdf , d: 1, v: 1, 
        maximum_length = 0
        char_map = {}
        
        left = 0
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            maximum_length = max(right - left + 1, maximum_length)
        return maximum_length 