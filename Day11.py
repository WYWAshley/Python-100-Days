# finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，
# finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），因此我们通常把finally块称
# 为“总是执行代码块”，它最适合用来做释放外部资源的操作。如果不愿意在finally代码块中关闭文件对
# 象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时
# 自动释放文件资源

import math

def is_prime(n):
    assert n > 0
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True if n != 1 else False

file_name = ('a.txt', 'b.txt', 'c.txt')
fs_ls = []
try:
    for file in file_name:
        fs_ls.append(open(file, 'w', encoding='utf-8'))
    for i in range(1, 10000):
        if is_prime(i):
            if i < 100:
                fs_ls[0].write(str(i)+'\n')
            elif i < 1000:
                fs_ls[1].write(str(i)+'\n')
            else:
                fs_ls[2].write(str(i)+'\n')
except Exception as e:
    print(e)
finally:
    for file in fs_ls:
        file.close()

