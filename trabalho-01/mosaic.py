#!/usr/bin/python3

from sys import argv
import cv2
import numpy as np


def get_args():
    if len(argv) != 3:
        print("Usage: python3 mosaic.py input output")
        exit(1)

    order = np.array([6, 11, 13, 3, 8, 16, 1, 9, 12, 14, 2, 7, 4, 15, 10, 5])

    return order, argv[1], argv[2]


def get_image_block_dimensions(image, n_rows, n_cols):
    height, width = image.shape
    image_block_h = int(height / n_cols)
    image_block_w = int(width / n_rows)

    return image_block_h, image_block_w


def build_mosaic(image, order, n_rows, n_cols):
    image_block_h, image_block_w = get_image_block_dimensions(image, n_rows, n_cols)
    mosaic = np.empty_like(image)

    for pre, new in enumerate(order):
        # getting new dimensions
        orig_row, orig_col = int(pre / n_rows), int(pre % n_cols)
        new_row, new_col = int(new / n_rows), int(new % n_cols)

        # allocating new positions
        orig_x_start, orig_x_end = orig_col * image_block_w, (orig_col + 1) * image_block_w
        orig_y_start, orig_y_end = orig_row * image_block_h, (orig_row + 1) * image_block_h

        new_x_start, new_x_end = new_col * image_block_w, (new_col + 1) * image_block_w
        new_y_start, new_y_end = new_row * image_block_h, (new_row + 1) * image_block_h

        # changing to new order
        mosaic[orig_y_start:orig_y_end, orig_x_start:orig_x_end] = image[new_y_start:new_y_end, new_x_start:new_x_end]

    return mosaic


def main():
    order, input, output = get_args()
    img = cv2.imread(input, 0)

    n_rows = 4
    n_cols = 4

    order = order - 1

    img = build_mosaic(img, order, n_rows, n_cols)

    cv2.imwrite(output, img)


if __name__ == '__main__':
    main()
