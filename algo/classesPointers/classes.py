import uuid


class Student:
    def __init__(self, usernmae):
        self.username = usernmae;


class Customer:
    def __init__(self):
        self.name = str.capitalize("Fas")
        self.id = uuid.uuid4()

    def set_name(self, name):
        self.name = name

    def set_id(self, cusId):
        self.id = cusId


class A:
    def __init__(self):
        print("outer class object creation")

    class B:
        def __init__(self):
            print("inner class object creation")

        def m1(self):
            print("inner class method")


class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


if __name__ == '__main__':
    std = Student("fas")
    cookie = Cookie("Blue")
    print(cookie.color)
