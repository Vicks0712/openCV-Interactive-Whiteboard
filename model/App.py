from model.shape_management.ToolManager import ToolManager
from model.user_interface.TrackbarManager import TrackbarManager
from Canvas import Canvas
import cv2
from model.recorder.Recorder import Recorder

class App:
    def __init__(self):
        self.canvas = Canvas()
        self.tool_manager = ToolManager(self.canvas)
        self.trackbars = TrackbarManager(self.canvas)
        self.recorder = Recorder(self.canvas)

    def run(self):
        self.trackbars.create_trackbars()

        while True:
            self.canvas.show()
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                self.recorder.stop_recording()
                break
            elif key == ord("s"):
                self.canvas.clear()
            elif key == ord("t"):
                self.canvas.toggle_fill()
            elif key == 13:
                if not self.recorder.is_recording:
                    self.recorder.start_recording()
                else:
                    self.recorder.stop_recording()

            self.tool_manager.select_tool(key)
            self.recorder.write_frame()