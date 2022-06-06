class CompareList:
    def items_in_common(self, param, param1):
        dic_first_list = {}
        for i in param:
            dic_first_list[i] = True
        for j in param1:
            if j in dic_first_list:
                return True
        return False


# Find common items in O(n)
if __name__ == '__main__':
    sln = CompareList()
    print(sln.items_in_common([2, 3, 4], [1, 2, 4]))
