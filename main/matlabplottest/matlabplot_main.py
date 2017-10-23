# -*- coding: utf-8 -*- f
__author__ = "DavidSmith"

from pylab import *


def main():
    x_values = arange(0.0, math.pi * 4, 0.01)
    y_values = sin(x_values)
    linewidth = 1.0
    plot(x_values, y_values)
    xlabel("x")
    ylabel("sin(x)")
    title("Simple plot")
    grid(True)

    show()

if __name__ == '__main__':
    main()