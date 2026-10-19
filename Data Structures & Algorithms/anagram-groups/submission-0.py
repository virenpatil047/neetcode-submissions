class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord('a')] += 1
            mpp[tuple(alpha)].append(s)
        return list(mpp.values())
