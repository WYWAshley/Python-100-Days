import numpy
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


"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'BBB', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
h = heapq.heapify(list1)
print(heapq.heappushpop(h, 3))
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))