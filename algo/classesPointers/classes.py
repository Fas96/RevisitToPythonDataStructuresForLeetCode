class Student:
    def __init__(self, usernmae):
        self.username = usernmae;

    def get_color(self):
        return self.username

    def set_color(self, user):
        self.username = user


class Cookie:
    def __init__(self, color):
        self.color = color


if __name__ == '__main__':
    std = Student("fas")
    std.set_color("Bhim nation")

    print(std.get_color())

    cookie = Cookie("Blue")
    print(cookie.color)
