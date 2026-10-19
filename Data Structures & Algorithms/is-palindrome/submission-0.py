class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True
        # cleaned = ""
        # for c in s:
        #     if c.isalnum():
        #         cleaned += c.lower()
        # for i in range(len(cleaned) // 2):
        #     if cleaned[i] != cleaned[len(cleaned) - i -1]:
        #         return False
        # return True