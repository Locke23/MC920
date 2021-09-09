#!/usr/bin/python3

from sys import argv
import cv2
import numpy as np


def get_args():
    if len(argv) != 4:
        print("Usage: python3 quantization.py K input output")
        exit(1)

    k = int(argv[1])

    if k < 2:
        print("K must be greater than 2")
        exit(1)

    return k, argv[2], argv[3]


def quantization(img, k):
    a = np.float32(img)

    bucket = 256 / k
    transformed = (a / (256 / k))
    return np.uint8(transformed) * bucket


def main():
    k, input, output = get_args()
    img = cv2.imread(input, 0)

    img = quantization(img, k)

    cv2.imwrite(output, img)


if __name__ == '__main__':
    main()
