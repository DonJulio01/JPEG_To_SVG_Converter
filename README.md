# Image Outline Tracer

A Python script that processes a JPEG image to detect and trace all lines where black meets white—including inner lines—and saves the traced outlines as an SVG file.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Script Explanation](#script-explanation)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)

## Description

The **Image Outline Tracer** script allows you to convert images with black outlines into scalable vector graphics (SVG). It detects all contours where black pixels meet white pixels, including both external and internal lines, and traces them into an SVG path.

## Features

- **Supports Multiple Image Formats**: Works with any image format supported by OpenCV (e.g., `.jpeg`, `.jpg`, `.png`).
- **Automatic Thresholding**: Utilizes Otsu's method for optimal threshold value selection.
- **Noise Reduction**: Applies Gaussian blur to improve contour detection.
- **Detailed Contours**: Captures both external and internal contours for comprehensive tracing.
- **Scalable Output**: Generates SVG files that can be scaled without loss of quality.

## Requirements

- **Python 3.x**
- **Libraries**:
  - `opencv-python`
  - `svgwrite`

## Installation

1. **Clone or Download the Script**:

   - Download the `trace_all_lines.py` script to your local machine.

2. **Install Required Libraries**:

   Open a terminal or command prompt and run:

   ```bash
   pip install opencv-python svgwrite
   ```

## Usage

1. **Prepare Your Image**:

   - Ensure your image has black lines on a white background.
   - Place the image in the same directory as the script or note its full file path.

2. **Run the Script**:

   ```bash
   python trace_all_lines.py input_image.jpeg output_image.svg
   ```

   - Replace `input_image.jpeg` with the path to your input image file.
   - Replace `output_image.svg` with the desired name for your output SVG file.

## Example

```bash
python trace_all_lines.py outline_image.jpeg traced_output.svg
```

This command processes `outline_image.jpeg` and creates an SVG file named `traced_output.svg` containing all traced lines.

## Script Explanation

The script performs the following steps:

1. **Imports Necessary Libraries**:

   ```python
   import cv2
   import svgwrite
   import sys
   ```

2. **Handles Command-Line Arguments**:

   - Expects two arguments: the input image filename and the output SVG filename.
   - Checks if the correct number of arguments is provided.

3. **Loads the Input Image**:

   ```python
   img = cv2.imread(input_image_filename)
   ```

   - Reads the image using OpenCV.
   - Verifies that the image was loaded successfully.

4. **Preprocesses the Image**:

   - **Converts to Grayscale**:

     ```python
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     ```

   - **Applies Gaussian Blur**:

     ```python
     gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
     ```

   - **Applies Otsu's Thresholding**:

     ```python
     ret, thresh = cv2.threshold(gray_blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
     ```

5. **Detects Contours**:

   ```python
   contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   ```

   - Retrieves all contours, including internal ones.
   - Uses contour approximation to reduce the number of points.

6. **Generates the SVG File**:

   - **Creates an SVG Drawing**:

     ```python
     dwg = svgwrite.Drawing(output_svg_filename, size=(width, height))
     ```

   - **Iterates Over Contours and Constructs Paths**:

     ```python
     for cnt in contours:
         # Process each contour
     ```

   - **Saves the SVG File**:

     ```python
     dwg.save()
     ```

## Customization

- **Adjust Thresholding Method**:

  - If the default thresholding doesn't yield desired results, you can switch to manual thresholding:

    ```python
    ret, thresh = cv2.threshold(gray_blurred, 127, 255, cv2.THRESH_BINARY_INV)
    ```

  - Replace `127` with a value between `0` and `255` to fine-tune.

- **Change Contour Approximation**:

  - For more detailed contours (results in larger SVG files):

    ```python
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    ```

- **Modify SVG Stroke Properties**:

  - Adjust stroke color and width:

    ```python
    path = dwg.path(fill='none', stroke='black', stroke_width=1)
    ```

  - Replace `'black'` with any valid SVG color and `1` with your desired stroke width.

## Troubleshooting

- **No Contours Detected**:

  - Ensure the image has a clear contrast between black lines and the background.
  - Try adjusting the threshold value or preprocessing steps.

- **Output SVG is Blank or Missing Details**:

  - Use `cv2.CHAIN_APPROX_NONE` for more detailed contours.
  - Verify that the input image is correctly specified and accessible.

- **Script Errors or Crashes**:

  - Confirm that all required libraries are installed.
  - Check for typos in the command-line arguments.

## License

This project is open-source and available under the [MIT License](LICENSE).