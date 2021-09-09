#!/usr/bin/python3

from sys import argv
import cv2


def get_args():
    if len(argv) != 4:
        print("Usage: python3 intensity.py type input output")
        exit(1)

    transform_type = int(argv[1])

    if (transform_type != 1) and (transform_type != 2):
        print("Type must be 1 to tranform to negative or 2 to convert the interval [100, 200]")
        exit(1)

    return transform_type, argv[2], argv[3]


def negative(image):
    image = 255 - image

    return image


def convert_interval(image):
    image = image / 2.56 + 100
    image = image.astype(int)

    return image


def main():
    transform_type, input, output = get_args()
    img = cv2.imread(input, 0)

    img = negative(img) if transform_type == 1 else convert_interval(img)

    cv2.imwrite(output, img)


if __name__ == '__main__':
    main()
