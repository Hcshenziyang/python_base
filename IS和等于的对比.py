# is None和==None的对比
class Foo:
    def __init__(self, num=10):
        self.num = num
    def __eq__(self, other):
        return True

f = Foo()
print(f == None)   # True（因为硬写成了True）
print(f is None)   # False（不是同一个对象）

# ==在python中，本质上是在result = obj.__eq__(other)，如同我们自己写了__eq__，那么就替换了结果
# is在python中实质是在对比内存地址，性能更高，不过用的很少，除了None对比或者单例模型。

