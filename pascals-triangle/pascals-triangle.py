class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        row always starts with 1 at front of array and 1 at end of array
        n + 1 row will always have length +1 from previous row
        first_two rows =  [1], [1,1] -> [1,2,1] -> [1,3,3,1], -> [1,4,6,4,1]
        '''
        num_1, num_2 = [1], [1,1]
        if numRows == 1: return [num_1]
        if numRows == 2: return [num_1, num_2]
        output = [num_1, num_2]
        for n in range(2, numRows):
            num_n = [1] * (n + 1)
            for i in range(len(num_n)):
                if i != 0 and i != len(num_n) - 1:
                    num_n[i] = num_2[i-1] + num_2[i]
            num_2 = num_n
            output.append(num_n)
        
        return output
        
        # num_2 = [1,3,3,1]