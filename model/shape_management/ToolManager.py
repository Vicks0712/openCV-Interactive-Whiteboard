from model.shape_management.CircleTool import CircleTool
from model.shape_management.PolygonTool import PolygonTool
from model.shape_management.RectangleTool import RectangleTool
from model.shape_management.LineTool import LineTool
from model.shape_management.FreehandTool import FreehandTool
from model.shape_management.EllipseTool import EllipseTool
import cv2

class ToolManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.tool_mapping = {
            ord("c"): CircleTool(self.canvas),
            ord("r"): RectangleTool(self.canvas),
            ord("l"): LineTool(self.canvas),
            ord("f"): FreehandTool(self.canvas),
            ord("e"): EllipseTool(self.canvas),
            ord("p"): PolygonTool(self.canvas),
        }
        self.current_tool = None

    def select_tool(self, key):
        if key in self.tool_mapping:
            if self.current_tool is not None:
                self.current_tool.finish_shape()
            self.current_tool = self.tool_mapping[key]
            cv2.setMouseCallback("Canvas", self.current_tool.handle_event)
