class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [(''.join(sorted(s)), s) for s in strs]
        
        groups = defaultdict(list)
        for ss, s in sorted_strs:
            groups[ss].append(s)
        
        return list(groups.values())