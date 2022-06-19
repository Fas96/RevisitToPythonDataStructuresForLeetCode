class Solution(object):
    def firstPalindrome(self, words):

        for s in words:
            if s==s[::-1]:
                return s

if __name__ == '__main__':
    sln = Solution()
    sln.firstPalindrome()
