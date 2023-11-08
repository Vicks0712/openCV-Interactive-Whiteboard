import cv2

class Recorder:
    def __init__(self, canvas):
        self.canvas = canvas
        self.is_recording = False
        self.video_writer = None
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.video_writer = cv2.VideoWriter('../../Videos/dibujo.mp4', self.fourcc, 30.0, (self.canvas.canvas.shape[1], self.canvas.canvas.shape[0]))

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.video_writer.release()

    def write_frame(self):
        if self.is_recording:
            self.video_writer.write(self.canvas.canvas)