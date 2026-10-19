class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        seen = []
        for b in s:
            if b in mp.keys():
                seen.append(b)
            else:
                if not seen or mp[seen[-1]] != b:
                    return False
                seen.pop()
        return seen == []