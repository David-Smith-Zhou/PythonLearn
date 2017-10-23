# -*- coding: utf-8 -*- f
import time
from my_sort import MySort


def get_src() -> list:
    src = []
    with open("source50.txt", "r") as file:
        for line in file:
            tmp = line[1:-1]
            tmp_split = tmp.split(",")
            for i in range(len(tmp_split)):
                src.append(int(tmp_split[i]))
            return src


def main():
    src = get_src()
    print("src: " + str(src))
    print("src len: " + str(len(src)))
    ms = MySort()
    start_time = time.time()
    rst = ms.bucket_sort(src)
    end_time = time.time()

    print("rst: " + str(rst))
    print("rst len: " + str(len(rst)))
    print("use time: " + str(end_time - start_time))

if __name__ == '__main__':
    main()