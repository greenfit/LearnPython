##encoding=utf-8

#打印乘法表
i = 1
while(i <= 9):
    j = 1
    while(j <= 9 and i >= j):
        print "%dX%d=%d" % (i, j, i*j),
        j = j + 1
    print ""
    i = i + 1

