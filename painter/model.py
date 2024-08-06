import math
import matplotlib.pyplot as plt
import pickle


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def area(self, radius: float) -> float:
        return math.pi * radius ** 2

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        self.x


        Circle with center at (x, y) and radius r
