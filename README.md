# OpenCV Interactive Whiteboard

![OpenCV](https://img.shields.io/badge/OpenCV-4.5.1-blue)

## Introduction

This project is a custom paint application developed using OpenCV, a powerful open-source computer vision and image processing library. The goal of this project is to create a versatile drawing toolset for users to create both basic and complex drawings. The application includes tools for drawing various shapes, changing colors, adjusting line thickness, and recording the drawing process.

## Model

The Model module contains the following classes and modules:

- **App.py**: Serves as the main entry point for the application, managing the canvas, tools, and recording functionality.
- **Canvas.py**: Handles the drawing canvas, allowing users to set colors, adjust line thickness, toggle shape filling, and clear the canvas.

### Mouse Movement

The Mouse Movement module includes the following class, used to record and operate with mouse movements:

- **MouseEventHandler.py**: Manages mouse event handling.
- **PointDrawer.py**: Handles drawing points.
- **PointManager.py**: Manages points for drawing.

### Recorder

The Recorder module includes the following class:

- **Recorder.py**: Handles video recording of the canvas, allowing users to capture their drawing process.

### Shape Management

The Shape Management module comprises various classes for drawing shapes:

- **CircleTool.py**: Draws circles.
- **EllipseTool.py**: Draws ellipses.
- **FreehandTool.py**: Draws freehand lines.
- **LineTool.py**: Draws straight lines.
- **PolygonTool.py**: Draws polygons with multiple points.
- **RectangleTool.py**: Draws rectangles.
- **ToolManager.py**: Manages the selection of different drawing tools.

### User Interface

The User Interface module includes the following classes:

- **TrackbarManager.py**: Creates trackbars for adjusting color and line thickness on the canvas.

## Objectives

The primary objectives of this project include:
1. Create a versatile drawing application using OpenCV.
2. Implement tools for drawing various shapes: circles, rectangles, lines, ellipses, and polygons.
3. Allow users to change the color of their drawings.
4. Enable users to adjust the line thickness for their drawings.
5. Provide an option to fill shapes with color.
6. Implement the recording of the drawing process as a video.

## Achievement of Objectives

Here's an evaluation of the project's objectives:

1. **Versatile Drawing Application:** The project successfully creates a drawing application with various tools and features.
   
2. **Shape Drawing Tools:** The project implements tools for drawing circles, rectangles, lines, ellipses, and polygons.

3. **Color Selection:** Users can change the color of their drawings using trackbars.

4. **Line Thickness Adjustment:** The project allows users to adjust the line thickness for their drawings using trackbars.

5. **Shape Filling:** Users can choose to fill shapes with color, as the project includes a "Toggle Fill" option.

6. **Video Recording:** The project enables users to record the drawing process as a video, which can be started and stopped by pressing the Enter key.

## How to Use

1. Ensure you have the OpenCV library (4.5.1) installed. You can install it using the following command:
   
   ```bash
   pip install opencv-python-headless==4.5.1
   ```
## How to Use

1. Run the main script to start the OpenCV Paint application.
2. Use the following keys to interact with the application:
   - Press the tool's corresponding key to select it (e.g., "c" for Circle, "r" for Rectangle).
   - Press "q" to stop video recording (if recording is active).
   - Press "s" to clear the canvas.
   - Press "t" to toggle fill for shapes.
   - Press Enter (Return) to start or stop video recording.
3. Use the trackbars within the application window to adjust the color and line thickness for your drawings.

## System Requirements

To use this project, you need:
- Python 3.x
- OpenCV 4.5.1
- A computer with a display for running the application.

## About OpenCV

OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It provides a wide range of tools for image and video analysis, including image processing, object detection, and more.

For more information about OpenCV, visit the official website: [OpenCV](https://opencv.org)

## Contributions

This project is open source, and we welcome contributions from the community. If you wish to improve the code, fix errors, or add new features, please do not hesitate to submit a pull request. Together, we can enhance this watch detector and make it even more accurate and versatile.
