import random

import numpy
import math


class MonteCarlo:
    def __init__(self, x_min, x_max, func, num_count):
        self.x_min = x_min
        self.x_max = x_max
        self.y_max = max([func(random.uniform(x_min, x_max)) for i in range(num_count)])
        self.y_min = 0
        self.func = func
        self.num_count = num_count
        self.in_zone = []
        self.out_zone = []

    def generate_points(self):
        points_array = [(random.uniform(self.x_max, self.x_min), random.uniform(self.y_min, self.y_max)) for i in
                        range(self.num_count)]
        a = 0
        for x, y in points_array:
            func_y = self.func(x)
            if y < func_y:
                self.in_zone.append((x, y))
            else:
                self.out_zone.append((x, y))

    def square(self):
        return (self.x_max - self.x_min) * self.y_max * len(self.in_zone) / self.num_count

