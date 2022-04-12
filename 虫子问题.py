# 幼虫 2 days
# 成熟 一天下一个仔 2 days
# 第五天 死亡 不下仔
# 幼虫到死亡 五天时间 下三个仔

# 用list实现 横轴表示时间 天
# 0, 0, 1, 0, 0            第0天   1 表示现在有一个成年幼虫
# 1, 0, 0, 1, 0            第一天
# 1, 1, 0, 0, 1            第二天
# 0, 1, 1, 0, 0            第三天
# 1, 0, 1, 1, 0            第四天

while True:
    try:
        days = int(input())
        bugs = [0, 0, 1, 0, 0]
        tmp = 0
        diebugs = 0
        for i in range(days):
            diebugs += bugs[4]
            tmp = bugs[0]
            bugs[0] = bugs[2] + bugs[3]
            bugs[4] = bugs[3]
            bugs[3] = bugs[2]
            bugs[2] = bugs[1]
            bugs[1] = tmp
        totallivebug = bugs[0] + bugs[1] +bugs[2] +bugs[3]
        print(f'目前活着的虫子数：{totallivebug}，已经死亡的虫子的总数{diebugs}')
    except:
        break
