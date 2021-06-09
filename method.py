class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def info(self):
        return f"My height is {self.height} and my width is {self.width}"


rect1 = Rectangle(100, 500)

print(rect1.info())
