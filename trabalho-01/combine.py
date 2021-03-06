#!/usr/bin/python3

from sys import argv
import cv2


def get_args():
    if len(argv) != 5:
        print("Usage: python3 combine.py percentage input_a input_b output")
        print("The percentage formula is:  percentage * img_a + (1 - percentage) * img_b")
        exit(1)

    percentage = float(argv[1])

    if percentage < 0 or percentage > 1:
        print("The percentage value must be a decimal number")
        exit(1)

    return percentage, argv[2], argv[3], argv[4]


def combine(percentage, img_a, img_b):
    combined = percentage * img_a + (1 - percentage) * img_b
    combined = combined.astype(int)

    return combined


def main():
    percentage, input_a, input_b, output = get_args()
    img_a = cv2.imread(input_a, 0)
    img_b = cv2.imread(input_b, 0)

    combined = combine(percentage, img_a, img_b)

    cv2.imwrite(output, combined)


if __name__ == '__main__':
    main()
