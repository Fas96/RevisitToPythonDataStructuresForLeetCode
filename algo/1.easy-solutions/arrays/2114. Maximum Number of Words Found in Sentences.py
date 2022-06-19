class Solution(object):
    def mostWordsFound(self, sentences):
        m = 0
        for s in sentences:
            m = max(m, list(s.split(" ")))
        return m


if __name__ == '__main__':
    sln = Solution()
    sln.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
