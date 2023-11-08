import cv2
import numpy as np

from model.mouse_movement.MouseEventHandler import MouseEventHandler
from model.mouse_movement.PointManager import PointManager


class PolygonTool(MouseEventHandler):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.point_manager = PointManager()

    def handle_event(self, event, x, y, flags, param):
        super().handle_event(event, x, y, flags, param)
        if event == cv2.EVENT_LBUTTONDOWN and self.drawing:
            self.point_manager.add_point(x, y)

    def draw_shape(self, x, y):
        canvas_copy = np.copy(self.temp_canvas)
        if self.point_manager.points:
            cv2.polylines(canvas_copy, [np.array(self.point_manager.points)], isClosed=False, color=self.canvas.color, thickness=self.canvas.line_thickness)
        self.canvas.canvas = canvas_copy

    def finish_shape(self):
        if len(self.point_manager.points) >= 3:
            canvas_copy = np.copy(self.temp_canvas)
            cv2.polylines(canvas_copy, [np.array(self.point_manager.points)], isClosed=True, color=self.canvas.color, thickness=self.canvas.line_thickness)
            if self.canvas.fill_shape:
                cv2.fillPoly(canvas_copy, [np.array(self.point_manager.points)], self.canvas.color)
            self.canvas.canvas = canvas_copy
            self.point_manager.clear_points()



