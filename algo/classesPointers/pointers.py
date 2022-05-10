def pointer():
    """Pointes of common variables does not modify in memory"""
    num = 11
    num2 = num
    print(num2, num)
    num = 22
    print(num2, num)


def dictionary():
    """Pointers to dictionary modify the memory values if any instance of a reference is modified"""
    dic1 = {'val': 11}
    dic2 = dic1
    print(dic1, dic2)
    print("Updates when we change dictionary one: It points to same memory")
    dic1['val'] = 300
    """Garbage collection for variables that are not used or reference at the end of execution"""
    print(dic1, dic2)
    dic3 = dic1;
    print(dic3, dic1)
    dic3['val'] = 90
    print(dic1, dic2, dic3)


if __name__ == '__main__':
    pointer()

    dictionary()
