# -*- coding: utf-8 -*- f


class Solution:
    def fibonacci(self, n):
        # write your code here
        x, y = 0, 1
        result = []
        count = 1
        if n < 0 and n is 0:
            print("n is not bigger than zero\n")
            return -1
        if n is 1:
            return x
        if n is 2:
            return y
        while count < n:
            result.append(y)
            x, y = y, y + x
            count += 1
        return result[count - 2]

    def spiral_matrix(self, n=int):
        print("n is %d\n" % n)
        print(rst + '\n')

