class Solution(object):
    def twoSum(self, numbers, target):
        dp = [[False] * target for x in range(len(numbers))]

        print(dp)
        res = []
        for i in range(len(numbers)):
            for j in range(target):
                if j + numbers[i] == target and j < target and j != numbers[i]:
                    print(numbers[i], j)
                    res.append(i + 1)
                    # res.append(numbers.index(j))
                    dp[i][j] = True
                    break
        print(res)


def subsetSum(numbers, t):
    lsum = sum(numbers)
    if lsum % 2 != 0:
        return False
    lsum = lsum // 2
    dp = [[False] * (lsum + 1) for x in range(len(numbers) + 1)]

    for i in range(len(numbers)):
        dp[i][0] = True

    for i in range(1, len(numbers)):
        for j in range(1, t):
            if j - numbers[i] >= 0:
                print(dp[i - 1][j], dp[i - 1][j - numbers[i - 1]])
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - numbers[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    return dp


# Note the arrays are sorted
class Solutions:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            if s > target:
                j -= 1
            else:
                i += 1
        return []


if __name__ == '__main__':
    # sln = Solution()
    # sln.twoSum([-1,0], -1)
    print(subsetSum([2, 3, 7, 8], 11))
