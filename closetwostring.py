class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        onemap = {}
        twomap = {}
        for ele in word1:
            if ele not in onemap:
                onemap[ele] = 1
            else:
                onemap[ele] += 1
        for ele in word2:
            if ele not in twomap:
                twomap[ele] = 1
            else:
                twomap[ele] += 1

        values = list(twomap.values())
        onevalues = list(onemap.values())
        for key, value in onemap.items():
            if key not in twomap:
                return False
            if value not in values:
                return False
            else:
                values.remove(value)

        for key, value in twomap.items():
            if key not in onemap:
                return False
            if value not in onevalues:
                return False
            else:
                onevalues.remove(value)
        return True


if __name__ == '__main__':
    word1 = "aaabbbbccddeeeeefffff"
    word2 = "aaaaabbcccdddeeeeffff"
    bob = Solution
    print(bob.closeStrings(bob, word1, word2))
