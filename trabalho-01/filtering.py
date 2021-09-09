#!/usr/bin/python3

from sys import argv
import cv2
import numpy as np


def _args():
    if len(argv) != 4:
        print("Usage: python3 bits.py filter input output")
        exit(1)

    filter = int(argv[1])

    if (filter < 0) or (filter > 2):
        print("The chosen filter must be 1 or 2")
        exit(1)

    return filter, argv[2], argv[3]


def first_filter(image):
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)


def second_filter(image):
    kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    return cv2.filter2D(image, -1, kernel)


def main():
    filter, input, output = _args()
    img = cv2.imread(input, 0)

    img = first_filter(img) if filter == 1 else second_filter(img)

    cv2.imwrite(output, img)


if __name__ == '__main__':
    main()
