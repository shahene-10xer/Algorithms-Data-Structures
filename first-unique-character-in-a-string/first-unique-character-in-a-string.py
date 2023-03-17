class Solution:
    def firstUniqChar(self, s: str) -> int:
        "leetcode"
        '''
        go through characters, add unique characters to set
        iterate through s, first char not in s, return i
        '''
        char_freq = collections.Counter(s)
        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i
        return -1 
        
        
            
                
            
        