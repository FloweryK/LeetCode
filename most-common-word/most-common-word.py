class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # lowercase only
        paragraph = paragraph.lower()
        
        # alphabet only
        paragraph = re.sub(r"[^a-z ]", " ", paragraph)
        
        # counter
        count = collections.Counter(paragraph.split())
        
        # erase banned key
        for key in banned:
            del count[key]
        
        # get max
        max_key = max(count, key=lambda x: count[x])
        
        return max_key