class Solution(object):
    def capitalizeTitle(self, title):
        tstr = title.split(" ")
        rs = ""
        for w in tstr:
            if len(w) > 2:
                rs = rs + " " + w.capitalize()
            else:
                rs =rs+" " +w.lower()
        print(rs)
        return rs.strip()


if __name__ == '__main__':
    sln = Solution()
    sln.capitalizeTitle("First leTTeR of EACH Word")
