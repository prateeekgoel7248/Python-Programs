class Solution:
    def pow(self, x, n, d):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x % d  # notice the modulo operation
        if n % 2 == 0:
            # power is even => calculate once for n/2 and then square it.
            half = self.pow(x, n//2, d)
            return (half * half) % d  # notice the modulo operation
        else:
            # power is odd => calculate once for ((n-1) / 2) (even), square it, then multiply by x.
            half = self.pow(x, (n-1) // 2, d)
            return (half * half * x) % d  # notice the modulo operation