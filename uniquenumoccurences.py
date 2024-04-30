class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        hmap = {}
        s = set()
        l = []
        for ele in arr:
            if ele not in hmap:
                hmap[ele] = 1
            else:
                hmap[ele] += 1

        for val in hmap.values():
            s.add(val)
            l.append(val)
        if len(s) != len(l):
            return False
        return True