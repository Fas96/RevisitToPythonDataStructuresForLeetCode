class Solution(object):
    def longestStrChain(self, words):
        words = sorted(words, key=len)
        k = 0
        for i in range(1, len(words)):
            p = words[i - 1]
            c = words[i]
            if len(p) == 0 and len(p) == len(c):
                k += 1
            common = self.lcs(p, c, len(p), len(c))
            if len(c) - len(p) == 1:
                k += 1
            print(abs(len(p) - len(c)), common,len(c),len(p), len(c) - len(p) == 1, k)

    def lcs(self, X, Y, m, n):
        if m == 0 or n == 0:
            return 0
        elif X[m - 1] == Y[n - 1]:
            return 1 + self.lcs(X, Y, m - 1, n - 1);
        else:
            return max(self.lcs(X, Y, m, n - 1), self.lcs(X, Y, m - 1, n));


if __name__ == '__main__':
    sln = Solution()
    sln.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])
