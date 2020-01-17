# https://leetcode.com/problems/minimum-path-sum

class Solution:
    
    m = 0
    n = 0
    
    nodeCost = []
    
    def smallerCost(self, x, y, grid):
        
        cost = grid[x][y]
        
        if(x == self.m and y == self.n):
            self.nodeCost[x][y] = cost
            return cost
        
        elif  (x == self.m):
            right_cost = self.nodeCost[x][y+1]
            if(right_cost == -1):
                right_cost = self.smallerCost(x, y + 1, grid)
            cost = cost + right_cost
        
        elif  (y == self.n):
            down_cost = self.nodeCost[x+1][y]
            if(down_cost == -1):
                down_cost = self.smallerCost(x + 1, y, grid)
            cost = cost + down_cost
        
        else:
            down_cost = self.nodeCost[x+1][y]
            right_cost = self.nodeCost[x][y+1]
            
            if(down_cost == -1):
                down_cost = self.smallerCost(x + 1, y, grid)
            
            if(right_cost == -1):
                right_cost = self.smallerCost(x, y + 1, grid)
            
            if(down_cost > right_cost):
                cost = cost + right_cost
            else:
                cost = cost + down_cost
                
        if(self.nodeCost[x][y] == -1 or self.nodeCost[x][y] > cost):
            self.nodeCost[x][y] = cost

        return cost
            
        
            
    def minPathSum(self, grid: List[List[int]]) -> int:
     
        self.m = len(grid) - 1
        self.n = len(grid[0]) - 1
        self.nodeCost = []
        
        for i in range(self.m + 1):
            self.nodeCost.append([-1] * (self.n + 1));

        
        return self.smallerCost(0, 0, grid)
     
