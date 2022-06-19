class Solution(object):
    def maxSubsequence(self, nums, k):
        # nums.sort()
        mx = float("-inf")
        mxlist = []

        for i in range(1 + len(nums) - k):
            sb = 0
            lisd = nums[i:i + k]
            for j in range(i, i + k):
                sb += nums[j]
            if sb > mx:
                mx = max(mx, sb)
                mxlist = lisd
        print(mxlist)
        return mxlist

    def maxSubsequencea(self, nums, k):
        for _ in range(len(nums) - k):
            target = min(nums)
            print(target)
            nums.remove(target)
        return nums


if __name__ == '__main__':
    sln = Solution()
    sln.maxSubsequencea([3, 3, 3, 4], 2)
