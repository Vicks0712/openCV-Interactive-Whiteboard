from model.mouse_movement.MouseEventHandler import MouseEventHandler
import cv2
import numpy as np


class RectangleTool(MouseEventHandler):
    def draw_shape(self, x, y):
        canvas_copy = np.copy(self.temp_canvas)
        if self.canvas.fill_shape:
            cv2.rectangle(canvas_copy, (self.start_x, self.start_y), (x, y), self.canvas.color, -1)
        else:
            cv2.rectangle(canvas_copy, (self.start_x, self.start_y), (x, y), self.canvas.color, self.canvas.line_thickness)
        self.canvas.canvas = canvas_copy

    def finish_shape(self):
        pass