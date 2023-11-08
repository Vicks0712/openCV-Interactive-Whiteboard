from model.mouse_movement.MouseEventHandler import MouseEventHandler
import cv2
import numpy as np

class EllipseTool(MouseEventHandler):
    def draw_shape(self, x, y):
        canvas_copy = np.copy(self.temp_canvas)
        center = ((self.start_x + x) // 2, (self.start_y + y) // 2)
        axes = (abs(x - self.start_x) // 2, abs(y - self.start_y) // 2)

        if self.canvas.fill_shape:
            cv2.ellipse(canvas_copy, center, axes, 0, 0, 360, self.canvas.color, -1)
        else:
            cv2.ellipse(canvas_copy, center, axes, 0, 0, 360, self.canvas.color, self.canvas.line_thickness)

        self.canvas.canvas = canvas_copy

    def finish_shape(self):
        pass