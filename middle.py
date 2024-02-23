# -*- coding: utf-8 -*-

from math import *
from PIL import Image


def draw_vec(x_, y_, angle, size, pix):
    if angle == '0':
        return
    x1, y1 = x_, y_
    for _ in range(4):
        x1 += cos(atan(angle))
        y1 += sin(atan(angle))
        if x1 < 0 or x1 >= size or y1 < 0 or y1 >= size:
            break
        pix[int(x1), int(y1)] = (0, 255, 0)

    x1 += cos(atan(angle))
    y1 += sin(atan(angle))
    if not (x1 < 0 or x1 >= size or y1 < 0 or y1 >= size):
        pix[int(x1), int(y1)] = (0, 0, 0)


def func_1(x, y, f, sos):
    x = x / sos
    y = y / sos
    try:
        return eval(f)
    except:
        return '0'


def func_2(x, y, y_p, f, sos):
    x = x / sos
    y = y / sos

    try:
        t = eval(f)

        if abs(t) < 0.1:
            return y_p, t
        else:
            return '0'
    except Exception as e:
        return '0'


def draw_izo_PIL(size, f, mode, sos, times_per_sos):
    image = Image.new('RGB', (size, size), 'white')
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    xhalf, yhalf = width // 2, height // 2

    for x in range(width):
        pix[x, yhalf] = (0, 0, 0)

    for y in range(height):
        pix[xhalf, y] = (255, 0, 0)

    for x in range(0, width, sos // times_per_sos):
        for y in range(0, height, sos // times_per_sos):
            if mode == 1:
                draw_vec(x, y, func_1(x - xhalf, y - yhalf, f, sos), size, pix)
            else:
                min_err = ('0', 1e18)
                for y_p in range(-1000, 1000, 1):
                    y_p /= 100
                    a = func_2(x - xhalf, y - yhalf, y_p, f, sos)
                    if a != '0':
                        if min_err[1] > a[1]:
                            min_err = a
                draw_vec(x, y, min_err[0], size, pix)


    y_top, y_bottom = 0, height - 1
    while y_top < y_bottom:
        for x in range(width):
            pix[x, y_top], pix[x, y_bottom] = pix[x, y_bottom], pix[x, y_top]
        y_top += 1
        y_bottom -= 1

    return image


if __name__ == '__main__':
    draw_izo_PIL(100, 'sin(x) + asin(y) - 2*y_p', 2, 20, 4).save('buffer.png')
