# -*- coding: utf8 -*-
def test_1(val):
    print "val", val, type(val)

def test_2(val):
    print "val", val, type(2)

if __name__ == "__main__":
    for i in [1, 2]:
        eval("test_" + str(i))(i)

'''
分析：利用eval函数，把字符串“test”和“1”组合成函数名test_1(test_2同样)，挺神奇的，第一次见到这么用。
'''
