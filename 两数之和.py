# 输入 int x
# 求数组中第一个出现的. 和为x 的 两个数
# 要求复杂度低于 n**2

# 复杂度为n的方法
# 显存字典 然后判断
while True:
    try:
        x = int(input())
        l1 = list(map(int, input().split(' ')))
        a = 0
        d1 = {}
        for i, num in enumerate(l1):
            if d1.get(x - num) is not None:
                print(num, x - num)
            d1[num] = i      # 这句不能放在if 之前 ，会出现  x -num = num # 输入 4 然后 1 2 1 1 会返回 2 2
    except:
        break
