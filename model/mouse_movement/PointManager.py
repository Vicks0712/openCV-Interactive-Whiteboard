class PointManager:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def clear_points(self):
        self.points = []