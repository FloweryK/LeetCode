class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            tmp = s[-(i+1)]
            s[-(i+1)] = s[i]
            s[i] = tmp
        """
        Do not return anything, modify s in-place instead.
        """
        