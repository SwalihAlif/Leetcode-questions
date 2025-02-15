#200. Number of Islands
class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = 0
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)
        num_of_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_of_island += 1
                    dfs(i, j)
        return num_of_island
        
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >=m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = 0
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)
        num_of_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_of_island += 1
                    dfs(i, j)
        return num_of_island

bt = Solution()        
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(bt.numIslands(grid))
