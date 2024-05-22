class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        t = 2 ** (n - 1)
        e = t / 2
        if k > e:
            return 1 - self.kthGrammar(n, k - e)
        return self.kthGrammar(n - 1, k)
