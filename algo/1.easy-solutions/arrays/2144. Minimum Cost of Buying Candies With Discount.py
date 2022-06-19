from collections import Counter


class Solution(object):
    def minimumCosta(self, cost):
        cost.sort(reverse=True)
        total_cost = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
        return total_cost

    def minimumCost(self, cost):
        cost.sort(reverse=True)
        i = 0
        j = len(cost) - 1
        tmin = 0
        Counter(cost)
        while True and len(cost) > 0:
            p1 = cost.pop()
            p2 = cost.pop()
            tmin += (p1 + p2)
            if len(cost) > 0 and (p1 + p2) / 2 > cost[-1]:
                cost.pop()
            else:
                tmin += cost.pop()
                break

        return tmin


if __name__ == '__main__':
    sln = Solution()
    print(sln.minimumCost([3, 3, 3, 1]))
