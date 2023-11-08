import numpy as np
import cv2

class Canvas:
    def __init__(self, width=500, height=500):
        self.canvas = np.ones((height, width, 3), dtype=np.uint8) * 255
        self.color = (0, 0, 0)  
        self.line_thickness = 2
        self.fill_shape = False

    def set_color(self, r, g, b):
        self.color = (b, g, r)

    def set_line_thickness(self, thickness):
        self.line_thickness = thickness

    def toggle_fill(self):
        self.fill_shape = not self.fill_shape

    def clear(self):
        self.canvas[:] = 255

    def show(self):
        cv2.imshow("Canvas", self.canvas)
