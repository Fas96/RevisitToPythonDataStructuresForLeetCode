class Solution(object):
    def findFinalValue(self, nums, original):

        while True:
            if original in nums:
                original *= 2
            else:
                break
        return original


if __name__ == '__main__':
    sln = Solution()
    sln.findFinalValue([2, 7, 9], 4)
