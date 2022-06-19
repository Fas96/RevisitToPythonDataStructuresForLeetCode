from collections import Counter


class Solution(object):
    def countWords(self, words1, words2):
        minString = min(len(words1), len(words2))
        loopmax = words2 if len(words2) > len(words1) else words1
        loopmin = words1 if len(words2) > len(words1) else words2
        print()

        timinCount = 0
        hash = {}
        for i in range(minString):
            if loopmax.count(loopmin[i]) == 1 and loopmin[i] not in hash:
                timinCount += 1
                hash[i] = loopmin[i]
        print(timinCount)
        return timinCount

    def skb(self, word1, word2):
        a, b = Counter(word1), Counter(word2)
        result = 0
        for key, val in a.items():
            if val != 1:
                continue
            print(b[key])
            if b[key] == 1:
                result += 1
        print(result)
        return result


if __name__ == '__main__':
    sln = Solution()
    sln.skb(["ibxyatvglhltxngewrcrqbbnew", "towokpjpkccmob", "kdmtwngzpebwpnvlazhdcmtwpjh", "muh",
             "fzzlmacbbvoqdueutjqoutwd", "ylluspdftxxqbwadivfdzulghq", "hioiacezaiptpsvcojzckhxz",
             "nzcjhjomaupevyekennyrfwyd", "tdwtuinstwsfyjnfkxkbnsptisuifo", "wrdwoxzsczzlnwjugopohxh", "p",
             "jkez", "drisymx", "fsva", "myqc", "aovjoxzpkylpecltwtottzidq", "wqspbhpberqjabockesc", "f",
             "qostobxgfliil", "gsekmhjpuedeivioudx", "tzelzowtgnvjsxgbw", "zgmpazgnioprk", "fucybddarjcve",
             "ldacfviysy", "yxyjairoxtvbkljaokca", "vxpiohhvjuwcpiceafcdzobalgpz", "wyflbpmkfwftndgtnftajgla",
             "xbxvvk", "bnrwyshimjamltmlugeiviu", "wsgqysmuakedrrmjk", "ppqmgibqljkwgmiwi", "fly", "uf",
             "tvvttzrsjbojve", "ztxtnmljdhyz", "vxonvloufeksfvg", "wql", "kotdenqjrdlgofubocb", "wlaqceczd",
             "mtmhtgvqwr", "aymzxpfvbqxydmilafyqvapuxtnqe", "ig", "atetjlhdcigunmmit", "enkdcxqnw",
             "gtlcmkxwvdhumgfurxkesmekmnhjo", "hurihasxncgtzleerslvwxkz", "zked", "xiaqvclhuhggcgoouzjgi",
             "mzejuubgyhvlfbecpmggddby", "boyotuukuiprtlvktypxboosw", "vwfceei", "gopsxsihawzhtlmdyiggljzggrhqr",
             "bckuuqszgncdhkeghudflczm", "e", "yvhwysrunkxsppbqjf", "lo", "bze", "kuzoqvgugnrpfkelktfg",
             "ntjtlwwmuevtsqujpxswgx", "zkdwtpdlvrfkbyktqsellmghaxj", "u", "rpmpq", "ajhlzwfrbysqloduofr",
             "gyfmhcskcrjepgeplbbj", "fe", "zyolvtetrdffy", "apbkyczsuvde", "fnkqf", "qwwxpwbr", "krkbnww",
             "zkvqkugfpziawiokdzlpjomfarkor", "jg", "l", "srbvxsnuhyqzmycvavmmakh", "dhkgzjrstir",
             "smaaptkzpwhukebwboysbnawgzgot"]
            , ["p", "towokpjpkccmob", "vflbjyecpzxnuay", "fzas", "fzzlmacbbvoqdueutjqoutwd", "bwjjzw", "va",
               "manrvuldjzrdnwihzct", "tdwtuinstwsfyjnfkxkbnsptisuifo", "wrdwoxzsczzlnwjugopohxh", "p",
               "tylcyihdjruhaayzcwxrynnkch", "uojzddpgyvqslha", "fsva", "rucvbjzfewjlhddxefhf", "tfihr",
               "wqspbhpberqjabockesc", "f", "bmfo", "zsjbzjmbloaybdofsrqvzwoizz", "tzelzowtgnvjsxgbw",
               "tproznqma", "lmryjiyvkgsxsaylkdmmxeub", "ldacfviysy", "xpamoswlugwjxyny", "rmfvgm", "wm",
               "xbxvvk", "ubawz", "jbrabb", "rgegpb", "fly", "aofydpklgjqmxhvxuhq", "tvvttzrsjbojve", "wj",
               "vxonvloufeksfvg", "wql", "vu", "nhuxqdfyftrbbodztyydb", "mtmhtgvqwr",
               "aymzxpfvbqxydmilafyqvapuxtnqe", "fqksatpfo", "ylzkfvvzdsryl", "enkdcxqnw",
               "gtlcmkxwvdhumgfurxkesmekmnhjo", "nccwybkxuawwdqyhrhmbt", "zked", "eyzwtvsjt", "qy",
               "boyotuukuiprtlvktypxboosw"])
