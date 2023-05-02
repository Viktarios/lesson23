class Point2D:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x=0):
        self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y=0):
        self.__y = y

    def __str__(self):
        return f"Point2D: x={self.__x}, y={self.__y}"
