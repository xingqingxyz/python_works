常数 = [1, 2, 3]


def squareroot(n):
    # 著名的牛顿迭代法
    root = n / 2
    for i in range(20):
        root = (root + n / root) / 2
    return root


#
#
# class First:
#     """
#     first time forever
#     """
#
#     def __init__(self):
#         pass
#
#     @property
#     def test1(self):
#         b = []
#         b = 常数.append(self)
#         return b


# if __name__ == "__mian__":
running: bool = True


class FuckError:
    pass


while running:
    try:
        a = squareroot(float(input("算数平方根:")))
    except ZeroDivisionError:
        running = False
    # bug:除去负数

    else:
        print(a)
