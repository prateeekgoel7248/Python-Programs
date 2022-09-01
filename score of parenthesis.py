class Solution(object):
    def scoreOfParentheses(self, S):
        res = l = 0
        for a, b in itertools.izip(S, S[1:]):
            if a + b == '()': res += 2 ** l
            l += 1 if a == '(' else -1
        return res
        