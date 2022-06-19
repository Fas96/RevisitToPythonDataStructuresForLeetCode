class Solution(object):
    def smallestEqual(self, nums):
        lsIndex = []

        for i in range(len(nums)):
            if i % 10 == nums[i]:
                lsIndex.append(i)
        print(lsIndex)
        return min(lsIndex) if len(lsIndex)>0 else -1


if __name__ == '__main__':
    sln = Solution()
    sln.smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
