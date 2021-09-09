#!/usr/bin/python3

from sys import argv
import cv2
import numpy as np


def _args():
    if len(argv) != 3:
        print("Usage: python3 entropy_calculus.py input output")
        exit(1)

    return argv[1], argv[2]


def calculate_image_entropy(img):
    marg = np.histogramdd(np.ravel(img), bins=256)[0] / img.size
    marg = list(filter(lambda p: p > 0, np.ravel(marg)))
    entropy = -np.sum(np.multiply(marg, np.log2(marg)))

    return entropy


def main():
    input, output = _args()
    img = cv2.imread(input, 0)

    entropy_value = calculate_image_entropy(img)

    with open(output, 'w') as f:
        f.write(str(entropy_value))


if __name__ == '__main__':
    main()
