#!/usr/bin/env python3

from sys import argv
import cv2


def get_args():
    if len(argv) != 4:
        print("Usage: python3 brightness.py gamma input output")
        exit(1)

    return float(argv[1]), argv[2], argv[3]


def brightness(image, gamma):
    image = step_a(image)

    image = step_b(image, gamma)

    image = step_c(image)

    return image


def step_a(image):
    # Reducing interval to [0,1]
    image = image / 2.55
    return image


def step_b(image, gamma):
    # Exponencial transformation
    image = image ** (1 / gamma)
    return image


def step_c(image):
    # converting results to interval [0, 255]
    size = image.max() - image.min()
    image = image * (255 / size)

    min = image.min()
    image = image - min
    image = image.astype(int)
    return image


def main():
    gamma, input, output = get_args()
    img = cv2.imread(input, 0)

    img = brightness(img, gamma)

    cv2.imwrite(output, img)


if __name__ == '__main__':
    main()
