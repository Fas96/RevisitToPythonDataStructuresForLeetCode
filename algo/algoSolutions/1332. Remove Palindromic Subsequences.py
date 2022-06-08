class LeetCode:
    def rps(self, s):
        subseqls = self.helperfnx(s)
        ls = list(set(subseqls))
        gls = []
        for i in ls:
            if len(i) > 1:
                gls.append(i)
        pl = self.palindromes(gls)
        countList = self.removePalindrome(s, pl)
        print(countList)
        vals = self.getCount(s, countList)
        print(vals)

    def helperfnx(self, s):
        if len(s) == 0:
            em = [""]
            return em
        ch = s[0]
        subs = s[1:]
        subss = self.helperfnx(subs)
        res = []
        for val in subss:
            res.append(val)
            res.append(ch + val)
        return res

    def palindromes(self, gls):
        pls = []
        for i in gls:
            if i == i[::-1]:
                pls.append(i)
        return pls

    def removePalindrome(self, s, pl):
        res = []
        for i in pl:
            if i in s:
                res.append(i)
        return res

    def getCount(self, s, countList):
        count = 0
        for i in countList:
            if i == s:
                return 1
        
        return count


if __name__ == '__main__':
    ltc = LeetCode()
    print(ltc.rps("baabb"))
