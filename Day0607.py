import random
import string
import time
import os

def generate(l):
    code = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ge = ''
    for i in range(0, l):
        num = random.randint(0, len(code))
        ge += code[num]
    print(ge)

    # python自带sample功能，从多个字符中生成指定数量的随机字符
    print(''.join(random.sample(string.ascii_letters + string.digits, 4)))

    # 随机浮点数：random.uniform(1, 10)
    # 随机选取字符串：random.choice(['剪刀', '石头', '布'])
    # 随机选取0到100间的偶数：random.randrange(0, 101, 2)
    # 打乱排序 items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] random.shuffle(items)

# generate(4)

def paomadeng():

    content = '北京欢迎您...'
    while True:
        i= os.system('cls')
        print(content)
        content = content[1:] + content[0]
        time.sleep(0.2)


# paomadeng()
# 在pycharm中会出现乱码问题，没有被清屏成功，但是在cmd中运行py文件就可行了
# 在idle中清屏的方法，看链接：https://blog.csdn.net/cxcxrs/article/details/81219395

def get_suffix(file_name, hasdot):
    pos = file_name.rfind(".")
    if 0 < pos < len(file_name) - 1:
        index = pos if hasdot else pos + 1
    print(file_name[index:])

# get_suffix("Day0607.py", False)


def find_max(lst):
    if len(lst) == 0:
        return "ERROR:EMPTY LIST!!!"
    m, ms = lst[0], lst[0]
    for item in lst:
        if m < item:
            ms = m
            m = item
        elif ms < item:
            ms = item
    print("MAX:%s, SEC:%s" % (m, ms))

# find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


def is_leap_year(year):
    return True if year%4==0 and year%100!=0 or year%400==0 else False

def count_days(str):
    year = int(str[0:4])
    month = int(str[5:7])
    day = int(str[8:10])

    days_1 = [0, 31,28,31,30,31,30,31,31,30,31,30,31]
    days_2 = [0, 31,29,31,30,31,30,31,31,30,31,30,31]

    res = 0
    if is_leap_year(year):
        for i in range(0, month):
            res += days_2[i]
    else:
        for i in range(0, month):
            res += days_1[i]
    print(res + day)

# count_days("2016/03/01")

def yanghuisanjiao(height):
    length = height * 2 - 1
    ls_1 = []
    ls_2 = []
    for i in range(0, height):
        ls_1 = ls_2.copy()
        ls_2.clear()
        ws = (length-1)//2 - i
        for j in range(0, ws):
            print(' ', end='')
        for j in range(0, i+1):
            if j == 0 or j == i:
                print(1, end=' ')
                ls_2.append(1)
            else:
                print(ls_1[j-1]+ls_1[j], end=' ')
                ls_2.append(ls_1[j-1]+ls_1[j])
        print()

# yanghuisanjiao(5)

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        print("%02d" % ball, end=' ')
        if index == len(balls) - 2:
            print('|', end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    select_ball = random.sample([x for x in range(1, 34)], 6)
    select_ball.sort()
    select_ball.append(randrange(1, 16))
    return select_ball


def yuesefuhuan(num):
    lst = [x for x in range(0, num)]
    start = 1
    for i in range(1, num//2 + 1):
        start = start + 8
        if start > len(lst)-1:
            start -= len(lst)
        lst.remove(lst[start])
    print(lst)
# yuesefuhuan(30)

# 约瑟夫环的单链表解法
# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.Next = None
# def create_linkList(num):
#     head = Node(1)
#     pre = head
#     for i in range(2, num+1):
#         newNode = Node(i)
#         pre.next = newNode
#         pre = newNode
#     pre.next = head
#     return head
# n = 5 #总的个数
# m = 2 #数的数目
# if m == 1: #如果是1的话，特殊处理，直接输出
#     print(n)
# else:
#     head = create_linkList(n)
#     pre = None
#     cur = head
#     while cur.next != cur: #终止条件是节点的下一个节点指向本身
#         for i in range(m-1):
#             pre = cur
#             cur = cur.next
#         pre.next = cur.next
#         cur.next = None
#         cur = pre.next
#     print(cur.value)


import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()







