from point2d import Point2D
import math


class Manager:
    @staticmethod
    def calculate_distance(point1, point2):
        if isinstance(point1, Point2D) and isinstance(point2, Point2D):
            dx = point1.x - point2.x
            dy = point1.y - point2.y
            # distance = (dx ** 2 + dy ** 2) ** 0.5
            distance = math.sqrt(dx ** 2 + dy ** 2)
            return distance

        return -1

class A:
    def __init__(self):
        self.filed = 0

    @staticmethod
    def method():
        pass