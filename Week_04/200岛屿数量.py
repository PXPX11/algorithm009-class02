#解法一
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs( grid, x, y):
            grid[x][y] = 0
            m = len(grid)
            n = len(grid[0])
            for new_x,new_y in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y] == '1':
                    dfs(grid,new_x,new_y)
        
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid,i,j)
        return count

