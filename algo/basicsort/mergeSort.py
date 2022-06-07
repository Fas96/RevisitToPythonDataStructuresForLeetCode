class MergeSort:
    def imp(self, ls):
        if len(ls) == 1:
            return ls
        mid = int(len(ls) / 2)
        left = ls[:mid]
        right = ls[mid:]
        return self.merge(self.imp(left), self.imp(right))

    def merge(self, ls1, ls2):
        combine = []
        i = 0
        j = 0
        while i < len(ls1) and j < len(ls2):
            if ls1[i] < ls2[j]:
                combine.append(ls1[i])
                i += 1
            else:
                combine.append(ls2[j])
                j += 1
        while i < len(ls1):
            combine.append(ls1[i])
            i += 1
        while j < len(ls2):
            combine.append(ls2[j])
            j += 1
        return combine


if __name__ == '__main__':
    mgSort = MergeSort()
    print(mgSort.imp([3, 1, 1, 3, 0, 6, 23, 4]))
