import numpy as np
import cv2


class MouseEventHandler:
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_x, self.start_y = -1, -1
        self.drawing = False
        self.temp_canvas = np.copy(self.canvas.canvas)

    def handle_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start_x, self.start_y = x, y
            self.drawing = True
            self.temp_canvas = np.copy(self.canvas.canvas)

        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.draw_shape(x, y)
            self.canvas.show()

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.draw_shape(x, y)
            self.temp_canvas = np.copy(self.canvas.canvas)

    def draw_shape(self, x, y):
        pass