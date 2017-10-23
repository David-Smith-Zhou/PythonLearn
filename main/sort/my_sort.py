# -*- coding: utf-8 -*- f
import math

class MySort:
    def __init__(self):
        pass

    def bubble_sort(self, src: list) -> list:
        dst = src.copy()
        for i in range(len(dst)):
            for j in range(len(dst)):
                if dst[i] < dst[j]:
                    tmp = dst[j]
                    dst[j] = dst[i]
                    dst[i] = tmp
        return dst

    def select_sort(self, lst: list) -> list:
        tmp = lst.copy()
        rst = []
        # tmp_min = tmp_max = 0

        while len(tmp) != 0:
            tmp_min = tmp_max = 0
            for i in range(len(tmp)):
                if tmp[i] > tmp[tmp_max]:
                    tmp_max = i
                if tmp[i] < tmp[tmp_min]:
                    tmp_min = i

            if len(rst) == 0:
                rst.append(tmp[tmp_min])
                rst.append(tmp[tmp_max])
                print("rst len: " + str(len(rst)))
                print("rst: " + str(rst))
            else:
                index = int(len(rst) / 2)
                print("index: " + str(index))
                rst.insert(index, tmp[tmp_min])
                if tmp[tmp_min] is not tmp[tmp_max]:
                    rst.insert(index + 1, tmp[tmp_max])
                print("rst len: " + str(len(rst)))
                print("rst: " + str(rst))
            print("tmp len: " + str(len(tmp)))
            print("tmp_min: " + str(tmp_min))
            tmp.pop(tmp_min)
            print("tmp_max: " + str(tmp_max))
            if tmp_min < tmp_max:
                tmp.pop(tmp_max - 1)
            else:
                if len(tmp) is not 0:
                    tmp.pop(tmp_max)
        return rst

    def insert_sort(self, lst: list) -> list:
        rst = []
        rst.append(lst[0])
        for i in range(1, len(lst)):
            for j in range(0, len(rst)):
                print("go into second for: i = %d, j = %d, lst size = %d, rst size = %d" % (i, j, len(lst), len(rst)))
                if lst[i] > rst[len(rst) - 1]:
                    rst.append(lst[i])
                if lst[i] < rst[0]:
                    rst.insert(0, lst[i])
                if (rst[j - 1] < lst[i]) and (lst[i] < rst[j]):
                    rst.insert(j, lst[i])
        return rst

    def merge_sort(self, lst: list) -> list:
        if len(lst) <= 1:
            return lst
        num = int(len(lst) / 2)
        left = self.merge_sort(lst[:num])
        right = self.merge_sort(lst[num:])
        return self.__merge(left, right)

    def __merge(self, left: int, right: int) -> list:
        r, l = 0, 0
        rst = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                rst.append(left[l])
                l += 1
            else:
                rst.append(right[r])
                r += 1
        # 若一个列表优先取完，另一个列表内的值无需比较直接追加在后面
        rst += right[r:]
        rst += left[l:]
        return rst

    def debug_log(self, src: str):
        with open("log.txt", "a") as file:
            file.write(src + "\n")

    def heap_sort(self, lst: list) -> list:
        size = len(lst)
        self.__heap_build(lst, size)
        # 这个len(lst) - 1很重要，不减一就会排序出错，这是一个需要注意的坑
        for i in range(len(lst) - 1, 0, -1):
            lst[0], lst[i] = lst[i], lst[0]
            self.__heap_max_heapify(lst, 0, i)
        return lst

    def __heap_build(self, lst: list, size: int):
        for i in range(int(len(lst) / 2), -1, -1):
            self.__heap_max_heapify(lst, i, size)

    def __heap_max_heapify(self, lst: list, index: int, size: int):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        largest = index
        if index < int(size / 2):
            if left_index < size and lst[left_index] > lst[largest]:
                largest = left_index
            if right_index < size and lst[right_index] > lst[largest]:
                largest = right_index
            if largest is not index:
                lst[index], lst[largest] = lst[largest], lst[index]
                self.__heap_max_heapify(lst, largest, size)

    # =======================================================================================================================
    # source code on the web
    # def __adjust_heap(self, lists, i, size):
    #     lchild = 2 * i + 1
    #     rchild = 2 * i + 2
    #     max = i
    #     if i < size / 2:
    #         if lchild < size and lists[lchild] > lists[max]:
    #             max = lchild
    #         if rchild < size and lists[rchild] > lists[max]:
    #             max = rchild
    #         if max != i:
    #             lists[max], lists[i] = lists[i], lists[max]
    #             self.__adjust_heap(lists, max, size)
    #
    # def __build_heap(self, lists, size):
    #     for i in range(0, int((size / 2)))[::-1]:
    #         self.__adjust_heap(lists, i, size)
    #
    # def heap_sort(self, lists):
    #     size = len(lists)
    #     self.__build_heap(lists, size)
    #     for i in range(0, size)[::-1]:
    #         lists[0], lists[i] = lists[i], lists[0]
    #         self.__adjust_heap(lists, 0, i)

    def quick_sort(self, lst: list) -> list:
        self.__quick_sort(lst, 0, len(lst) - 1)
        return lst

    def __quick_sort(self, lst: list, p: int, r: int):
        print("quick_sort: p = %d, r = %d" % (p, r))
        if p < r:
            # 根据选取的值确定第二次分治时的界限
            q = self.__quick_sort_partition(lst, p, r)
            self.__quick_sort(lst, p, q - 1)
            self.__quick_sort(lst, q + 1, r)

    def __quick_sort_partition(self, lst: list, p: int, r: int) -> int:
        print("quick_sort_partition: p = %d, r = %d" % (p, r))
        x = lst[r]
        i = p - 1
        for j in range(p, r):
            if lst[j] <= x:
                i = i + 1
                print("cur x is %d, exchange: No.%d = %d and No.%d = %d" % (x, i, lst[i], j, lst[j]))
                lst[i], lst[j] = lst[j], lst[i]
                print("list: " + str(lst))

        print("exchange: No.%d = %d and No.%d = %d" % (i + 1, lst[i + 1], r, lst[r]))
        lst[i + 1], lst[r] = lst[r], lst[i + 1]
        print("list: " + str(lst))
        return i + 1

    def counting_sort(self, src_list: list) -> list:
        # content_length = 0
        k = len(src_list)
        dst_list = ([0] * k)
        backup_list = ([0] * k)
        for j in range(0, len(src_list)):
            # print("#1 src_list[j] = %d" % (src_list[j]))
            backup_list[src_list[j]] = backup_list[src_list[j]] + 1
            # print("#1 backup_list: " + str(backup_list))
        for i in range(1, len(backup_list)):
            backup_list[i] = backup_list[i] + backup_list[i - 1]
            # print("#2 backup_list: " + str(backup_list))
        for m in range(len(src_list) - 1, -1, -1):
            # print("m = %d, src_list[m] = %d, backup_list[src_list[m]] = %d"
            #       % (m, src_list[m], backup_list[src_list[m]]))
            # 这个地方的减一，是通过debug发现的索引大了一，整体的数组往后移了一个单位，还不知道原因是什么
            dst_list[backup_list[src_list[m]] - 1] = src_list[m]
            backup_list[src_list[m]] = backup_list[src_list[m]] - 1
            # print("#3 backup_list: " + str(backup_list))
            # print("#3 dst_list: " + str(dst_list))
        return dst_list

    def radix_sort(self, src_list: list) -> list:
        max = self.__radix_get_max(src_list)
        loop_time = int(math.ceil(math.log(max, 10)))
        # print("loop_time: ", loop_time)
        dst_list = src_list.copy()
        self.__radix_sort(dst_list, 10, loop_time)
        return dst_list

    def __radix_sort(self, dst_list: list, radix: int, loop_times: int):
        for j in range(0, loop_times):
            radixs = [[] for j in range(radix)]
            for k in dst_list:
                # print("k / (radix ** j) % radix = ", k / (radix ** j) % radix)
                radixs[int(k / (radix ** j) % radix)].append(k)
                # print("radix size = ", len(radixs))
            # for i in range(0, 10):
                # print("radix: " + str(radixs[i][:]))
            del dst_list[:]
            for m in range(0, len(radixs)):
                dst_list.extend(radixs[:][m])
        return dst_list


    def __radix_get_max(self, src_list) -> int:
        max = src_list[0]
        for i in range(1, len(src_list)):
            if src_list[i] > max:
                max = src_list[i]
        return max

    def bucket_sort(self, src_list) -> list:
        n = len(src_list)
        buckets = [[] for _ in range(n)]
        for a in src_list:
            buckets[int(n * a)].append(a)
        dst_list = []
        for b in buckets:
            dst_list.extend(self.insert_sort(b))
        return dst_list


