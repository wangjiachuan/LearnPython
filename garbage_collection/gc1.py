# -*- coding: utf8 -*-
import gc
import sys

class CGcLeak(object):
    def __init__(self):
        self._text = '#' * 10

    def __del__(self):
        pass

def make_circle_ref():
    _gcleak = CGcLeak()
    print "_gcleak ref count0: %d" %(sys.getrefcount(_gcleak))
    del _gcleak
    try:
        print "_gcleak ref count1 :%d" %(sys.getrefcount(_gcleak))
    except UnboundLocalError:           # 本地变量xxx引用前没定义
        print "_gcleak is invalid!"
def test_gcleak():
    gc.enable()                         #设置垃圾回收器调试标志
    gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_INSTANCES | gc.DEBUG_OBJECTS)

    print "begin leak test..."
    make_circle_ref()

    print "\nbegin collect..."
    _unreachable = gc.collect()
    print "unreachable object num:%d" %(_unreachable)
    print "garbage object num:%d" %(len(gc.garbage))   #gc.garbage是一个list对象，列表项是垃圾收集器发现的不可达（即垃圾对象）、但又不能释放(不可回收)的对象，通常gc.garbage中的对象是引用对象还中的对象。因Python不知用什么顺序来调用对象的__del__函数，导致对象始终存活在gc.garbage中，造成内存泄露 if __name__ == "__main__": test_gcleak()。如果知道一个安全次序，那么就可以打破引用焕，再执行del gc.garbage[:]从而清空垃圾对象列表
if __name__ == "__main__":
    test_gcleak()
