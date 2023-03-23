class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # use bounds, top, left, right, bottom
        # go from left to right, then top to bottom, then right to left, then bottom to top
        # left += 1, top += 1, right -=. 1, bottom -= 1
        result = []
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        while left < right and top < bottom:
            # left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            # top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            # for edge case: matrix is single row or single column
            if not (left < right and top < bottom):
                break
            
            # right to left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # bottom to top
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result