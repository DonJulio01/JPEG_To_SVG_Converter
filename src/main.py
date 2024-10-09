import cv2
import svgwrite
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python scriptname.py input_image.jpeg output_image.svg")
        sys.exit(1)
    input_image_filename = sys.argv[1]
    output_svg_filename = sys.argv[2]

    img = cv2.imread(input_image_filename)
    if img is None:
        print(f"Error: Unable to load image {input_image_filename}")
        sys.exit(1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    height, width = thresh.shape

    dwg = svgwrite.Drawing(output_svg_filename, size=(width, height))

    for cnt in contours:
        points = cnt[:, 0, :]
        if len(points) < 2:
            continue
        path = dwg.path(fill='none', stroke='black', stroke_width=1)
        p = points[0]
        path.push('M', p[0], p[1])
        for p in points[1:]:
            path.push('L', p[0], p[1])
        path.push('Z')
        dwg.add(path)

    dwg.save()
    print(f"SVG file saved as {output_svg_filename}")


if __name__ == "__main__":
    main()
