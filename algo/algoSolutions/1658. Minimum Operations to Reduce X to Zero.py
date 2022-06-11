class Solution(object):
    def minOperations(self, nums, x):
        minOp = 0
        print(sum(nums)-x)


        i = 0
        j = len(nums) - 1
        while i < j or x > -1:
            ld = x - nums[i]

            rd = x - nums[j]
            if ld < 0 or rd < 0:
                break
            # print(nums)
            if rd == ld:
                j -= 1
                i += 1
                x -= nums.pop()
                # nums.pop(0)
                minOp += 1
                print(nums, x)
            else:
                if ld > rd:
                    j -= 1
                    x -= nums.pop()
                    minOp += 1
                else:
                    i += 1
                    x -= nums.pop(0)
                    minOp += 1
        return -1 if minOp == 0 else minOp

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum, max_len = 0, 0
        start_idx = 0
        found = False
        for end_idx in range(len(nums)):
            curr_sum += nums[end_idx]
            while start_idx <= end_idx and curr_sum > target:
                curr_sum -= nums[start_idx]
                start_idx += 1
            if curr_sum == target:
                found = True
                max_len = max(max_len, end_idx - start_idx + 1)

        return len(nums) - max_len if found else -1

if __name__ == '__main__':
    sln = Solution()
    print(sln.minOperations([3, 2, 20, 1, 1, 3], 10))
