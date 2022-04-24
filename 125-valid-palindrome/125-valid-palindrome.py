class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphas = ''
        for c in s:
            if c.isalnum():
                alphas += c
        
        return alphas.lower() == alphas[::-1].lower()