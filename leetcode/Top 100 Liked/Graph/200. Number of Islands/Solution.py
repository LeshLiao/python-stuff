from typing import List

class Solution:
    def __init__(self):
        self.visited = set()
        self.dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.maxRow = len(grid)
        self.maxColumn = len(grid[0])

        for i in range(self.maxRow):
            for j in range(self.maxColumn):
                if (i,j) not in self.visited and grid[i][j] == "1":
                    print(f"{i},{j}")
                    count += 1
                    self.dfs(i, j, grid)

        return count

    def dfs(self, i ,j , grid):
        if (i,j) in self.visited:
            return
        self.visited.add((i,j))

        for (r, c) in self.dir:
            newRow = i + r
            newColumn = j + c
            if (
                0 <= newRow < self.maxRow
                and 0 <= newColumn < self.maxColumn
                and (newRow,newColumn) not in self.visited
                and grid[newRow][newColumn] == "1"
            ):
                self.dfs(newRow,newColumn, grid)

test_cases = [
    ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 2),
    ([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 3),
]

for i, (p1, expected) in enumerate(test_cases, 1):
    sol = Solution()
    result = sol.numIslands(p1)
    if (result == expected):
        print(f"({i}) passed")
    else:
        print(f"({i}) failed. Result:{result}")
