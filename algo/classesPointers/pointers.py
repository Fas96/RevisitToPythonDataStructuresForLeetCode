def pointer():
    num = 11
    num2 = num
    print(num2, num)
    num = 22
    print(num2, num)


def dictionary():
    dic1 = {'val': 11}
    dic2 = dic1
    print(dic1, dic2)
    print("Updates when we change dictionary one: It points to same memory")
    dic1['val'] = 300
    print(dic1, dic2)
    dic3 = dic1;
    print(dic3, dic1)
    dic3['val'] = 90
    print(dic1, dic2, dic3)


if __name__ == '__main__':
    pointer()

    dictionary()
