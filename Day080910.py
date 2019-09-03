# coding=utf-8
# import time
#
# class clock(object):
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def show(self):
#         print("%02d:%02d:%02d" % (self._hour, self._minute, self._second))
#
#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
# __str__方法和__init__方法类似，都是一些特殊方法，所以前后都有双下划线，它用来返回对象的字符串表达式
# 如果要把一个类的实例变成 str，就需要实现特殊方法__str__() 而不使用__str__()方法
# def __str__(self):
#     return '(%d:%d:%d)' % (str(self._hour), str(self._minute), str(self._second))

# c = clock(23, 59, 50)
# while True:
#     c.show()
#     c.run()
#     time.sleep(1)


# class stu(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#     @property
#     def age(self):
#         return 2019-self._birth
#
# s = stu()
# s.birth = 1996
# print(s.birth)
# print(s.age)
# s.birth = 1995
# print(s.age)
# print(s.birth)


# 在python中，它是使用字典来保存一个对象的实例属性的。这非常有用，因为它允许我们我们在运行时去设置任意的新属性。
# 但是，这对某型已知属性的类来说，它可能是一个瓶颈。因为这个字典浪费了很多内存。
# python不能在对象创建的时候直接分配一个固定量的内存来保存所有属性，因此如果你有成千上万的属性的时候，它就会消耗很多内存。
# 有一个办法可以规避这个问题，就是使用__slots__来告诉python不要使用字典，而是只给一个固定集合的属性分配空间。
# 下面是个例子感受一下：https://www.jianshu.com/p/c0e5f7addb54
# Python 3.4.3 (default, Jun  6 2015, 13:32:34)
# Type "copyright", "credits" or "license" for more information.
#
# IPython 4.0.0 -- An enhanced Interactive Python.
# ?         -> Introduction and overview of IPython's features.
# %quickref -> Quick reference.
# help      -> Python's own help system.
# object?   -> Details about 'object', use 'object??' for extra details.
#
# In [1]: import ipython_memory_usage.ipython_memory_usage as imu
#
# In [2]: imu.start_watching_memory()
# In [2] used 0.0000 MiB RAM in 5.31s, peaked 0.00 MiB above current, total RAM usage 15.57 MiB
#
# In [3]: %cat slots.py
# class MyClass(object):
#         __slots__ = ['name', 'identifier']
#         def __init__(self, name, identifier):
#                 self.name = name
#                 self.identifier = identifier
#
# num = 1024*256
# x = [MyClass(1,1) for i in range(num)]
# In [3] used 0.2305 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 15.80 MiB
#
# In [4]: from slots import *
# In [4] used 9.3008 MiB RAM in 0.72s, peaked 0.00 MiB above current, total RAM usage 25.10 MiB
#
# In [5]: %cat noslots.py
# class MyClass(object):
#         def __init__(self, name, identifier):
#                 self.name = name
#                 self.identifier = identifier
#
# num = 1024*256
# x = [MyClass(1,1) for i in range(num)]
# In [5] used 0.1758 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 25.28 MiB
#
# In [6]: from noslots import *
# In [6] used 22.6680 MiB RAM in 0.80s, peaked 0.00 MiB above current, total RAM usage 47.95 MiB


# class Person(object):
#
#     # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
#
#
# def main():
#     person = Person('王大锤', 22)
#     person.play()
#     person._gender = '男'
#     # AttributeError: 'Person' object has no attribute '_is_gay'
#     person._is_gay = True

# coding=gbk
# import random
#
#
# class Card(object):
#     """一张牌"""
#
#     def __init__(self, suite, face):
#         self._suite = suite
#         self._face = face
#
#     @property
#     def face(self):
#         return self._face
#
#     @property
#     def suite(self):
#         return self._suite
#
#     def __str__(self):
#         if self._face == 1:
#             face_str = 'A'
#         elif self._face == 11:
#             face_str = 'J'
#         elif self._face == 12:
#             face_str = 'Q'
#         elif self._face == 13:
#             face_str = 'K'
#         else:
#             face_str = str(self._face)
#         return '%s%s' % (self._suite, face_str)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Poker(object):
#     """一副牌"""
#
#     def __init__(self):
#         self._cards = [Card(suite, face)
#                        for suite in '♠♥♣♦'
#                        for face in range(1, 14)]
#         self._current = 0
#
#     @property
#     def cards(self):
#         return self._cards
#
#     def shuffle(self):
#         """洗牌(随机乱序)"""
#         self._current = 0
#         random.shuffle(self._cards)
#
#     @property
#     def next(self):
#         """发牌"""
#         card = self._cards[self._current]
#         self._current += 1
#         return card
#
#     @property
#     def has_next(self):
#         """还有没有牌"""
#         return self._current < len(self._cards)
#
#
# class Player(object):
#     """玩家"""
#
#     def __init__(self, name):
#         self._name = name
#         self._cards_on_hand = []
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def cards_on_hand(self):
#         return self._cards_on_hand
#
#     def get(self, card):
#         """摸牌"""
#         self._cards_on_hand.append(card)
#
#     def arrange(self, card_key):
#         """玩家整理手上的牌"""
#         self._cards_on_hand.sort(key=card_key)
#
#
# # 排序规则-先根据花色再根据点数排序
# def get_key(card):
#     return (card.suite, card.face)
#
#
# def main():
#     p = Poker()
#     p.shuffle()
#     players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
#     for _ in range(13):
#         for player in players:
#             player.get(p.next)
#     for player in players:
#         print(player.name + ':', end=' ')
#         player.arrange(get_key)
#         print(player.cards_on_hand)
#
#
# if __name__ == '__main__':
#     main()

import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
