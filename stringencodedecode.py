class Solution:

    def encode(self, strs) -> str:
        if not strs:
            return 'NDE'
        s = ''
        for ele in strs:
            if ele is not strs[-1]:
                s += ele
                s += '~'
            else:
                s += ele
        return s

    def decode(self, s: str):
        if s == "":
            return [""]
        if s == 'NDE':
            return []
        l = s.split('~')
        return l
