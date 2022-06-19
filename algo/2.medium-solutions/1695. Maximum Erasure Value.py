class Solution:
    def maximumUniqueSubarray(self, nums):
        # TLE
        mx = float("-inf")

        for i in range(len(nums)):
            h = {}
            l = i
            while l < len(nums):
                if nums[l] in h.values():
                    break
                h[nums[l]] = nums[l]
                l += 1
            mx = max(mx, sum(h.values()))
        print(mx)
        return mx

    def maximumUniqueSubarrayS(self, nums):
        stkSet = set()
        lf = rl = res = sm = 0
        tlen = len(nums)

        while rl < tlen:
            cur = nums[rl]

            if cur not in stkSet:
                stkSet.add(cur)
                sm += cur
                res = max(res, sm)
                rl += 1
            else:
                stkSet.remove(nums[lf])
                sm -= nums[lf]
                lf += 1
        return res

if __name__ == '__main__':
    sln = Solution()
    sln.maximumUniqueSubarray([4, 2, 4, 5, 6])
