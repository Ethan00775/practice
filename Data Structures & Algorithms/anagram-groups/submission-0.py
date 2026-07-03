class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            num = [0] * 26
            for c in s:
                num[ord(c) - ord('a')] += 1
            f = tuple(num)
            if f not in groups:
                groups[f] = []
            groups[f].append(s)
        return list(groups.values())