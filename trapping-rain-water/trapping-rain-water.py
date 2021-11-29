class Solution:
    def trap(self, height: List[int]) -> int:
        # naive solution
        max_height = max(height)
        max_index = height.index(max_height)
        
        ans = 0
        
        # left side
        max_left = 0
        for i in range(0, max_index):
            if height[i] > max_left:
                max_left = height[i]
            else:
                ans += (max_left - height[i])
        
        # right side
        max_right = 0
        for i in range(len(height)-1, max_index, -1):
            if height[i] > max_right:
                max_right = height[i]
            else:
                ans += (max_right - height[i])
        
        return ans
        
#         # solution using stack
#         stack = []
        
#         ans = 0
#         for i in range(len(height)):
#             while stack and (height[i] > height[stack[-1]]):
#                 j = stack.pop()
                
#                 if not stack:
#                     break
                
#                 h_diff = min(height[i], height[stack[-1]]) - height[j]
#                 distance = i-stack[-1]-1
#                 ans += distance * h_diff
#             stack.append(i)
        
#         return ans
        