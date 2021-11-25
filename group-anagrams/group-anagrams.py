class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())
        
#         # Naive solution
#         anagrams = {}
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
            
#             if sorted_word in anagrams:
#                 anagrams[sorted_word].append(word)
#             else:
#                 anagrams[sorted_word] = [word]
        
#         return list(anagrams.values())