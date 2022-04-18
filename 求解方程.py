'''
求解方程
输入str ； 还有 x 和 x的系数，只有 + - 操作
输出x的值：
'''

while True:
    try:
        s = input()
        left, right = s.split('=')
        left = left.replace('-', '+-').split('+')
        right = right.replace('-', '+-').split('+')
        l_x, r_x, l_num, r_num = 0, 0, 0, 0

        for i in left:
            if i == 'x':
                l_x += 1
            elif i == '-x':
                l_x -= 1
            elif 'x' in i:
                l_x += int(i.split('x'))
            else:
                l_num += int(i)

        for j in right:
            if j == 'x':
                r_x += 1
            elif j == '-x':
                r_x -= 1
            elif 'x' in j:
                r_x += int(j.split('x'))
            else:
                r_num += int(j)

        if l_x == r_x and l_num == r_num:
            print('x = Infinite solutions')
        elif l_x != r_x and l_num == r_num:
            print('x = 0')
        elif l_x == r_x and l_num != r_num:
            print('No Solution')
        else:
            ans = (r_num - l_num) / (l_x - r_x)
            print('x = ', str(int(ans)))

    except:
        break
