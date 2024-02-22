import os.path
from math import *
from PIL import Image


def draw_izo_PIL(size, f):
    image = Image.new('RGB', (size, size), 'white')
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    def draw_vec(x_, y_, angle):
        if angle == '0':
            return
        x1, y1 = x_, y_
        for radius in range(4):
            x1 += cos(atan(angle))
            y1 += sin(atan(angle))
            if x1 < 0 or x1 >= size or y1 < 0 or y1 >= size:
                break
            pix[int(x1), int(y1)] = (0, 255, 0)

        x1 += cos(atan(angle))
        y1 += sin(atan(angle))
        if not (x1 < 0 or x1 >= size or y1 < 0 or y1 >= size):
            pix[int(x1), int(y1)] = (0, 0, 0)

    xhalf, yhalf = width // 2, height // 2

    for x in range(width):
        pix[x, yhalf] = (0, 0, 0)

    for y in range(height):
        pix[xhalf, y] = (255, 0, 0)

    def func(x, y):
        x = x / 10
        y = y / 10
        try:
            return eval(f)
        except:
            return '0'
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            draw_vec(x, y, func(x - xhalf, y - yhalf))
    y_top, y_bottom = 0, height - 1
    while y_top < y_bottom:
        for x in range(width):
            pix[x, y_top], pix[x, y_bottom] = pix[x, y_bottom], pix[x, y_top]
        y_top += 1
        y_bottom -= 1
    return image
if __name__ == '__main__':
    draw_izo_PIL(500).save('amongus.png')