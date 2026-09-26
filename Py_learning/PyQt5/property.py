#@property = decorator used to define a method as a property (it can be accessed like an attribute)
#           benefit: Add additional logic when read, write or delete attributes
#           Gives you getter, setter, and a de;eter method


class Rectangle:
    def __init__(self, width, height):
        #to ptivate a variable you do it with _
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:1f} cm"

    @property
    def height(self):
        return f"{self._height:1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width >= 0:
            self._width = new_width
        else:
            print("Height must tbe greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height >= 0:
            self._width = new_height
        else:
            print("Height must tbe greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("The width was deleted")


rectangle = Rectangle(3, 4)

print(rectangle.height)
print(rectangle.width)

rectangle.width = 12

print(rectangle.height)
print(rectangle.width)