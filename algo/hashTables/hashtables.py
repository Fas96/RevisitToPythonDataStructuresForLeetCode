class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, keys):
        my_hash = 0
        for letter in keys:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index]
        return None

    def HT_keys(self):
        keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for ls in self.data_map[i]:
                    keys.append(ls[0])
        return keys

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.set_item("fas", 32)
    hashtable.set_item("fas", 23)
    hashtable.set_item("fas", 23)
    hashtable.set_item("fas", 23)
    hashtable.set_item("fas", 23)
    hashtable.set_item("fas", 23)
    hashtable.set_item("fas", 23)
    hashtable.set_item("fs", 32)
    hashtable.set_item("s", 32)
    hashtable.set_item("Bhim", 32)
    hashtable.set_item("fs", 3333)
    hashtable.print_table()
    print("==========")
    print(hashtable.get_item("s"))
    print("=======")
    print(hashtable.HT_keys())
