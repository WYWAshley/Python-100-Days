import numpy
import math
#
# # 选择排序
# def selection_sort(origion_items, cmp=lambda x,y: x>y):
#     for i in range(len(origion_items)-1):
#         min_item = origion_items[i]
#         min_index = i
#         for j in range(i+1, len(origion_items)):
#             if cmp(min_item, origion_items[j]):
#                 min_item = origion_items[j]
#                 min_index = j
#         origion_items[i], origion_items[min_index] = origion_items[min_index], origion_items[i]
#     return origion_items
#
#
# # 鸡尾酒排序，冒泡排序的优化，在基本有序的初始列表有优势
# # 排序过程：
# # 先对数组从左到右进行冒泡排序（升序），则最大的元素去到最右端
# # 再对数组从右到左进行冒泡排序（降序），则最小的元素去到最左端
# # 以此类推，依次改变冒泡的方向，并不断缩小未排序元素的范围，直到最后一个元素结束
# def bubble_sort(origin_items, cmp=lambda x,y: x>y):
#     for i in range(len(origin_items)-1):
#         swapped = False
#         for j in range(i, len(origin_items)-1-i):
#             if cmp(origin_items[j], origin_items[j+1]):
#                 origin_items[j], origin_items[j+1] = origin_items[j+1], origin_items[j]
#                 swapped = True
#         if swapped:
#             for j in range(len(origin_items)-2-i, i, -1):
#                 if cmp(origin_items[j], origin_items[j + 1]):
#                     origin_items[j], origin_items[j - 1] = origin_items[j - 1], origin_items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return origin_items
#
#
# # 归并排序
# def merge_sort(origin_items, cmp=lambda x,y:x>y):
#     i = len(origin_items)
#     if i == 1:
#         return origin_items
#     left = merge_sort(origin_items[:i//2], cmp)
#     right = merge_sort(origin_items[i//2:], cmp)
#     merge = []
#     i = 0
#     j = 0
#     while len(left) > i and len(right) > j:
#         if cmp(left[i], right[j]):
#             merge.append(right[j])
#             j += 1
#         else:
#             merge.append(left[i])
#             i += 1
#
#     # 这一步python的list比c++的数组方便
#     # 但是注意这里不能用append，因为append不能用于迭代对象
#     merge += left[i:]
#     merge += right[j:]
#
#     return merge
#
#
# # 顺序查找
# def seq_search(items, key):
#     for index, num in enumerate(items):
#         if key == num:
#             return index
#     return -1
#
#
# # 折半查找
# def bin_search(items, key):
#     if len(items) == 1:
#         if items[0] == key:
#             return 0
#         else:
#             return -1
#     min = len(items) // 2
#     if items[min] == key:
#         return min
#     elif items[min] > key:
#         return bin_search(items[:min], key)
#     else:
#         x = bin_search(items[min:], key)
#         return lambda x: x+min if x!=-1 else -1
#
#
# def main():
#     origin_items = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
#     print(selection_sort(origin_items))
#     print(bubble_sort(origin_items))
#     print(merge_sort(origin_items))
#
#     print(seq_search(origin_items, 9))
#     origin_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(bin_search(origin_items, 5))
#
#
# if __name__ == '__main__':
#     main()


# # 使用生成式语法
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)
# # list1 = ['AAPL', 'GOOG', 'IBM', 'ORCL', 'ACN', 'FB', 'SYMC']
# list1 = [key for key in prices.keys()]
# # list2 = [191.88, 1186.96, 149.24, 48.44, 166.89, 208.09, 21.29]
# list2 = [value for value in prices.values()]
# price3 = {key: value for key in list1 for value in list2 if key == 'AAPL'}
# print(price3)
#
#
# # 嵌套的列表
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
# # scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = numpy.random.randn()
# print(scores)


# """
# 从列表中找出最大的或最小的N个元素
# 堆结构(大根堆/小根堆)
# """
# import heapq
#
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'BBB', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# h = heapq.heapify(list1)
# print(heapq.heappushpop(h, 3))
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


# # 五人分鱼，穷举法例子
# f = 6
# enough = False
# while not enough:
#     enough = True
#     fish = f
#     for _ in range(5):
#         fish -= 1
#         if fish <= 0 or fish % 5 != 0:
#             enough = False
#             break
#         fish = fish // 5 * 4
#     if enough:
#         print(f)
#     f += 5


# # 小偷快速找到满意解
# class thing(object):
#     def __init__(self, name, value, weight):
#         self._name = name
#         self._value = value
#         self._weight = weight
#     @property
#     def value(self):
#         return self._value
#     @property
#     def weight(self):
#         return self._weight
#
# def chioce():
#     ls_name = ['电脑', '收音机', '钟', '花瓶', '书', '油画']
#     ls_value = [200, 20, 175, 50, 10, 90]
#     ls_weight = [20, 4, 10, 2, 1, 9]
#     ls = []
#     for i in range(len(ls_name)):
#         ls.append(thing(ls_name[i], ls_value[i], ls_weight[i]))
#     ls = sorted(ls, key=lambda x: x.value/x.weight)
#
#     for i in range(len(ls)):
#         print(ls[i].value)
#
# chioce()


# # 分治法，快速排序
# def quick_sort(origin_items, cmp=lambda x,y: x>y):
#     if len(origin_items) <= 1:
#         return origin_items
#
#     pivot = origin_items[0]
#     i, j = 1, len(origin_items)-1
#     while i < j:
#         while i < len(origin_items) and cmp(pivot, origin_items[i]):
#             i += 1
#         while j > 0 and cmp(origin_items[j], pivot):
#             j -= 1
#         if i < j:
#             origin_items[i], origin_items[j] = origin_items[j], origin_items[i]
#     origin_items[0], origin_items[j] = origin_items[j], origin_items[0]
#
#     left = []
#     right = []
#     if i > 0:
#         left = quick_sort(origin_items[:j])
#     if i < len(origin_items) - 1:
#         right = quick_sort(origin_items[j+1:])
#
#     return left + [origin_items[j]] + right
#
# print(quick_sort([2, 5, 9, 1, 6, 3]))


# """
# 递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
# """
# import sys
# import time
#
# SIZE = 5
# total = 0
#
#
# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()
#
#
# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and col >= 0 and col < SIZE and board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法: ')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
#
#
# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#
#
# if __name__ == '__main__':
#     main()


# 自顶向下的备忘录法

# def number_tower():
#     case_num = int(input("例子数"))
#     for _ in range(case_num):
#         level_num = int(input("层数"))
#         ls = []
#         l = []
#         dp = [[0 for _ in range(j+1)] for j in range(level_num)]
#         for i in range(level_num):
#             for _ in range(i+1):
#                 n = int(input("输入编号，按回车键"))
#                 l.append(n)
#             c = l.copy()
#             # 得先复制一个c，否则l被清空，ls也不会保留了
#             ls.append(c)
#             l.clear()
#
#         dp[0][0] = ls[0][0]
#         for i in range(1, level_num):
#             for j in range(i+1):
#                 if j == 0:
#                     dp[i][j] = dp[i-1][0]+ls[i][j]
#                 elif j == i:
#                     dp[i][j] = dp[i-1][i-1] + ls[i][j]
#                 else:
#                     dp[i][j] = max(dp[i-1][(j-1)//2] + ls[i][j],
#                                    dp[i-1][(j+1)//2] + ls[i][j])
#
#         print(max(dp[level_num-1]))
#
# number_tower()


a = '12'

b = a
a += "3"
print(b)






