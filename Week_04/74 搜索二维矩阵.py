#方法一
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:return False
        m, n  = len(matrix),len(matrix[0])
        left , right = 0, m * n - 1
        while left <= right:
            mid = (left + right)//2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return False

#方法二 从右上角开始
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m= len(matrix)
        if m == 0 : return False
        n = len(matrix[0])
        if n == 0:
            return False
        h = 0
        w = n - 1
        while h < m and w >= 0:
            if matrix[h][w] == target:return True
            elif matrix[h][w] <= target:
                h += 1
            else:
                w -= 1
        return False