import math

class Polygon:
    def __init__(self, n, radius):
        self.n = n
        self.r = radius

    @property
    def edges(self):
        return self.n

    @property
    def vertices(self):
        return self.n

    @property
    def int_angle(self):
        return 180 * ((self.n - 2) / self.n)

    @property
    def edge_length(self):
        return 2 * self.r * math.sin(math.pi / self.n)

    @property
    def apothem(self):
        return self.r * math.cos(math.pi / self.n)

    @property
    def area(self):
        return self.edge_length * self.apothem * self.n / 2

    @property
    def perimeter(self):
        return self.edge_length * self.n

    def __repr__(self):
        return f"Polygon({self.n}, {self.r})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.n == other.n and self.r == other.r
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.n > other.n
        else:
            return False


class Polygons:
    def __init__(self, n, radius):
        self._l = [Polygon(i, radius) for i in range(3, n + 1)]

    def __getitem__(self, item):
        return self._l[item]

    def __len__(self):
        return len(self._l)

    def get_max(self):
        return (sorted(self._l, key=lambda x: x.area/x.perimeter, reverse=True))[0]
