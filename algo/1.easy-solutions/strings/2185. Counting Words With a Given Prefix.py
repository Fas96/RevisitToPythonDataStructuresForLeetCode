class Solution:
    def prefixCount(self, words, pref):
        ctn = 0
        for word in words:
            if word.startswith(pref):
                ctn += 1
        return ctn


if __name__ == '__main__':
    sln = Solution()
    sln.prefixCount(["leetcode", "win", "loops", "success"], "code")
