import matplotlib.pyplot as plt
import pickle

class Point:
    def __init__(self, x:float, y:float):
        self.x: float = x
        self.y: float = y

class Circle:
    def __init__(self, center:Point, radius:float):
        self.center: Point = center
        self.radius: float = radius


