from collections import defaultdict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        adj = defaultdict(list)
        left = set()
        visited = [True for _ in range(m*n)]
        
        for i in range(m):
            for j in range(n):
                if int(grid[i][j]):
                    adj[i*n+j].append(i*n+j)
                    left.add(i*n+j)
                    visited[i*n+j] = False
                    
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
        
        while left or stack:
            if not stack:
                answer += 1
                i = left.pop()
            else:
                i = stack.pop()
            
            visited[i] = True
                
            for j in adj[i]:
                if not visited[j]:
                    visited[j] = True
                    left.remove(j)
                    stack.append(j)
        
        return answer