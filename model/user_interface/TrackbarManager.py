import cv2
import numpy as np


class TrackbarManager:
    def __init__(self, canvas):
        self.canvas = canvas

    def create_trackbars(self):
        cv2.namedWindow("Canvas")
        cv2.createTrackbar("R", "Canvas", 0, 255, self.set_color)
        cv2.createTrackbar("G", "Canvas", 0, 255, self.set_color)
        cv2.createTrackbar("B", "Canvas", 0, 255, self.set_color)
        cv2.createTrackbar("Thickness", "Canvas", 1, 10, self.set_line_thickness)

    def set_color(self, value):
        r = cv2.getTrackbarPos("R", "Canvas")
        g = cv2.getTrackbarPos("G", "Canvas")
        b = cv2.getTrackbarPos("B", "Canvas")
        self.canvas.set_color(r, g, b)

    def set_line_thickness(self, value):
        thickness = cv2.getTrackbarPos("Thickness", "Canvas")
        self.canvas.set_line_thickness(thickness)