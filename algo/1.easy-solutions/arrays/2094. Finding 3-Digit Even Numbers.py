from itertools import permutations, combinations


class Solution(object):
    def findEvenNumbers(self, digits):
        lst = list(permutations(digits, 3))
        cb = list(combinations(digits, 3))
        print(cb)
        res = []
        for l in set(lst):
            sVal = int("".join(map(str, l)))
            print(l[0])
            if sVal % 2 == 0 and l[0]!= 0:
                res.append(sVal)
        res.sort()
        print(res)
        return res


if __name__ == '__main__':
    sln = Solution()
    sln.findEvenNumbers([2, 1, 3, 0])
