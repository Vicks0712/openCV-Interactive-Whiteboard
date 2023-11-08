import cv2
import numpy as np


class PointDrawer:
    def __init__(self, canvas, point_manager):
        self.canvas = canvas
        self.point_manager = point_manager

    def draw_points(self):
        canvas_copy = np.copy(self.canvas.temp_canvas)
        for point in self.point_manager.points:
            cv2.circle(canvas_copy, point, 5, self.canvas.color, -1)
        self.canvas.canvas = canvas_copy

