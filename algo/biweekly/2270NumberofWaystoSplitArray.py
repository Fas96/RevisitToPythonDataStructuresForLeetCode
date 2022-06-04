class Solution:
    def waysToSplitArray(self, nums):

        res = 0

        for i in range(1, len(nums)-1):
            if sum(nums[:i]) >= sum(nums[i:]):
                res += 1
        return res


if __name__ == '__main__':
    soln = Solution()
    print(soln.waysToSplitArray([-100000, 100000]))
