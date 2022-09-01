class Solution(object):
    def kWeakestRows(self, mat, k):
        def binary_search(row): # this will be O(logN) where N is no of col
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi)//2
                if row[mid]: lo = mid + 1
                else: hi = mid
            return lo

        temp = sorted([(binary_search(row), i) for i, row in enumerate(mat)]) # Is this M*log(M) where M is no of row?
        return [i for v, i in temp][:k]
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        