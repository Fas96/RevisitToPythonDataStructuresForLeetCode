class Solution:
    def removeDuplicateLetters(self, s) -> str:
        dicRes = dict((letter, s.count(letter)) for letter in set(s))
        uniqueR = set(s)
        print(uniqueR)
        # find last index of each unique item
        # if
        indeU = []
        for c in uniqueR:
            indeU.append({c: s.rindex(c)})
        print(indeU)


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicateLetters("cbacdcbc")