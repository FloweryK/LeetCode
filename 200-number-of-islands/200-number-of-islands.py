from collections import defaultdict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        adj = defaultdict(list)
        not_visited = set()
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if int(grid[i][j]):
                    not_visited.add(i*n+j)
                    adj[i*n+j].append(i*n+j)
                    
                    if i-1 >= 0 and int(grid[i-1][j]):
                        adj[i*n+j].append((i-1)*n+j)
                        
                    if i+1 <= m-1 and int(grid[i+1][j]):
                        adj[i*n+j].append((i+1)*n+j)
                        
                    if j-1 >= 0 and int(grid[i][j-1]):
                        adj[i*n+j].append(i*n+(j-1))
                        
                    if j+1 <= n-1 and int(grid[i][j+1]):
                        adj[i*n+j].append(i*n+(j+1))
                   
        answer = 0
        stack = []
        
        while not_visited or stack:
            if not stack:
                answer += 1
                i = not_visited.pop()
            else:
                i = stack.pop()
                
            for j in adj[i]:
                if j in not_visited:
                    not_visited.remove(j)
                    stack.append(j)
        
        return answer