class Factorial:
    def fact(self, num):
        if num <= 1:
            return num
        return self.fact(num - 1) * num


if __name__ == '__main__':
    fc = Factorial()
    print(fc.fact(4))
