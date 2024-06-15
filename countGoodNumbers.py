class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def power(x, y):
            if y == 0:
                return 1
            p = power(x, y // 2) % mod
            p = (p * p) % mod
            if y % 2 == 0:
                return p
            else:
                return ((x * p) % mod)
        return (power(5, (n + 1) // 2) * power(4, n // 2)) % mod
