# import time
# import threading
#
#
# class Account(object):
#     def __init__(self):
#         self._balance = 0
#         self._lock = threading.Lock()
#
#     def deposit(self, money):
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             time.sleep(0.01)
#             self._balance = new_balance
#         finally:
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThreading(threading.Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._money = money
#         self._account = account
#
#     def run(self):
#         self._account.deposit(self._money)
#
#
# def main():
#     account = Account()
#     threads = []
#     for _ in range(100):
#         t = AddMoneyThreading(account, 1)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print(account.balance)
#
#
# if __name__ == '__main__':
#     main()


import openpyxl

