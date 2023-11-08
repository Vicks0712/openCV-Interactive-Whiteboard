from model.mouse_movement.MouseEventHandler import MouseEventHandler
import cv2
import numpy as np


class CircleTool(MouseEventHandler):
    def draw_shape(self, x, y):
        canvas_copy = np.copy(self.temp_canvas)
        radius = int(np.sqrt((x - self.start_x) ** 2 + (y - self.start_y) ** 2))
        if self.canvas.fill_shape:
            cv2.circle(canvas_copy, (self.start_x, self.start_y), radius, self.canvas.color, -1)
        else:
            cv2.circle(canvas_copy, (self.start_x, self.start_y), radius, self.canvas.color, self.canvas.line_thickness)
        self.canvas.canvas = canvas_copy

    def finish_shape(self):
        pass