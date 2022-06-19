class Solution(object):
    def countValidWords(self, sentence):
        letters = [chr(97 + i) for i in range(0, 26)]
        digits = [i for i in range(0, 10)]
        hypPunct = ['-', '!', '.', ',']
        Punct = ['-', '!', '.', ',']
        wordToken = sentence.split(' ')

        cnt = 0
        wordToken = [n for n in wordToken if len(n) > 0]
        print(wordToken)
        for w in wordToken:
            if not any(char.isdigit() for char in w):
                print(w, "--")
                if any(char in hypPunct for char in w):
                    if any(char in Punct for char in w):
                        indLs = []
                        chLs = []
                        for ww in w:
                            if ww in Punct:
                                indLs.append(w.find(ww))
                            else:
                                chLs.append(w.find(ww))
                        res = False
                        for i in indLs:
                            if any(i < char for char in chLs):
                                res = True
                        if not res:
                            cnt += 1
                    else:
                        indexHyp = w.find('-')
                        if indexHyp != -1:
                            if w[(indexHyp-1)].isalpha() and w[(indexHyp+1)].isalpha():
                                cnt += 1
            if all(char.isalpha() for char in w):
                cnt += 1

        return cnt


if __name__ == '__main__':
    sln = Solution()
    ans = sln.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.")
    print(ans)
