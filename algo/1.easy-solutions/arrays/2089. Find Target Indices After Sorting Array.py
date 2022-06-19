class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        idx=[]
        for i in range(len(nums)):
            if target==nums[i]:
                idx.append(i)
        print(idx)
        return idx

if __name__ == '__main__':
    sln = Solution()
    sln.targetIndices([1, 2, 5, 2, 3], 2)
