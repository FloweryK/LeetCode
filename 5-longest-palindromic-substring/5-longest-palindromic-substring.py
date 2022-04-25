class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        for k in reversed(range(1, len(s)+1)):
            for i in range(len(s)-(k-1)):
                subset = s[i:i+k]
                if subset == subset[::-1]:
                    return subset
                
                