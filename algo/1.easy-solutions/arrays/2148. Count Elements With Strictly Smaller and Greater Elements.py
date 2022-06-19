from collections import Counter


class Solution(object):
    def countElements(self, nums):
        nums.sort()
        ccd = Counter(nums)
        print(len(ccd))
        p = Counter(nums).get(nums[0])
        e = Counter(nums).get(nums[-1])
        if len(nums) == 0:
            return 0
        return len(nums) - p - e


if __name__ == '__main__':
    sln = Solution()
    print(sln.countElements([-3, 3, 3, 90]))
