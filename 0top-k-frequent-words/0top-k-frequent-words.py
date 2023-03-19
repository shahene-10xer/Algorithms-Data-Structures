class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = collections.Counter(words)
        heap = []
        
        for word in word_freq:
            heapq.heappush(heap, (word_freq[word] * -1, word))
        print(heap)
        output = []
        for _ in range(k):
            next_word = heapq.heappop(heap)[1]
            output.append(next_word)
        
        return output
            