class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        num_sec = 0
        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[i] != 0:
                    tickets[i] -= 1
                    num_sec += 1
            print(tickets)
        print(num_sec)
        return num_sec


if __name__ == '__main__':
    sln = Solution()
    sln.timeRequiredToBuy([2, 3, 2], 2)
