class Solution:
    def compress(self, chars: List[str]) -> int:
        i = index = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            
            chars[index] = chars[i]
            index += 1
            if j - i > 1:
                count = str(j - i)
                for digit in count:
                    chars[index] = digit
                    index += 1
            
            i = j
        
        return index 
    