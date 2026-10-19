class Solution:

    def encode(self, strs: List[str]) -> str:
        encd = ""
        for s in strs:
            for c in s:
                encd += chr(ord(c) + 4)
            encd += '*_*'
        return encd

    def decode(self, s: str) -> List[str]:
        decd = []
        encd = s.split('*_*')
        encd = encd[:-1]
        for s in encd:
            d = ""
            for c in s:
                d += chr(ord(c) - 4)
            decd.append(d)
        return decd
