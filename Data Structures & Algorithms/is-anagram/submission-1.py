class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpp = {}
        for i in s:
            if i not in mpp:
                mpp[i] = 1
            else:
                mpp[i] += 1
        for i in t:
            if i not in mpp:
                return False
            else:
                mpp[i] -= 1
        for k in mpp.keys():
            if mpp[k] != 0:
                return False
        return True