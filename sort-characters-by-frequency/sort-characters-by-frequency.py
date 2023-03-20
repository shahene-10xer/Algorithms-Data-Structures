from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        Create Frequency Counter
        Place characters into a max-heap
        Build string with array
        Return sorted string
        Time -> O(n)
        Space -> O(n)
    '''
        s_count = Counter(s)
        maximum_string_c = []
        string_builder = []
        
        for char in s_count:
            heapq.heappush(maximum_string_c, (-1 * s_count[char], char))
        while maximum_string_c:
            count, popped_string = heapq.heappop(maximum_string_c)
            string_builder.append(popped_string * (-1 * count))
        
        return ''.join(string_builder)
        