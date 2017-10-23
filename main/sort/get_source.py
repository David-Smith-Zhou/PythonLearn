# -*- coding: utf-8 -*- f

import random

RANGE = 50


def main():
    sources = random.sample([i for i in range(RANGE)], RANGE)
    print(sources)
    with open("source" + str(RANGE) + ".txt", "x") as output:
        output.write(str(sources))

if __name__ == '__main__':
    main()