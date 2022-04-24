from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-z]', ' ', paragraph.lower())
        paragraph = [par for par in paragraph.split(' ') if par]
        
        counter = Counter(paragraph)
        for word in banned:
            del counter[word]
        
        return counter.most_common(1)[0][0]
