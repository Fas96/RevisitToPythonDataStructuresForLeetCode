class Solution(object):
    def checkAlmostEquivalenta(self, word1, word2):
        w1 = {chr(97 + i): 0 for i in range(0, 26)}
        w2 = {chr(97 + i): 0 for i in range(0, 26)}
        print(w2)
        print(w1)
        for i in word1:
            w1[i] += 1
        for i in word2:
            w2[i] += 1
        for i in w1:
            if abs(w1[i] - w2[i]) > 3:
                return False
        return True

    def checkAlmostEquivalent(self, word1, word2):
        freqword1 = self.getFreq(word1)
        freqword2 = self.getFreq(word2)
        print(freqword1, freqword2)
        ll1 = list(freqword1.keys())
        ll2 = list(freqword2.keys())
        if not self.commonEl(ll2, ll1):
            return False

        for k, v in freqword1.items():
            if k in freqword2.keys():
                diff = abs(v - freqword2[k])
                if diff > 3:
                    return False
            else:
                if v > 3:
                    return False
        return True

    def commonEl(self, l, l2):
        for x in l:
            if x in l2:
                return True
        return False

    def getFreq(self, word):
        h = {}
        for w in word:
            if w not in h.keys():
                h[w] = 1
            else:
                h[w] += 1
        return h


if __name__ == '__main__':
    sln = Solution()
    print(sln.checkAlmostEquivalenta("aaaab", "zzzza"))
