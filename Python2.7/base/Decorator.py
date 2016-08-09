#encoding=utf-8

def info():
    print "调用Info"
    return "info()"

print "---普通模式---"
res = info()
print "调用结果为:" + res;
print "--------------"

def decoInfo(function):
    print "[DEBUG] 调用函数之前"
    return function

print "---装饰器模式---"
info = decoInfo(info)#只调用一次装饰器的代码 ???
print "--- 完成装饰 ---"
res = info()#此处仍为旧的代码 ???
res2 = info()
print "调用结果为:" + res;
print "调用结果为:" + res2;
print "----------------"



