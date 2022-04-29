#  输入四个0-10的数字 输出能否组成24点
#  思路是 利用递归反推

# def helper(arr, item):
#     # if item < 1:
#     #     return False
#     if len(arr) == 1:
#         return arr[0] == item
#     for i in range(len(arr)):
#         L = arr[:i] + arr[i+1:]
#         v = arr[i]
#         if helper(L, item - v):
#             return True
#         elif helper(L, item + v):
#             return True
#         elif helper(L, item * v):
#             return True
#         elif helper(L, item / v):
#             return True
#
#
# while True:
#     try:
#         a = list(map(int, input().split()))
#         if helper(a, 24):
#             print('true')
#         else:
#             print('false')
#     except:
#         break


### 写出表达式
import itertools
import numpy as np


def make_num(nums, target):
    print(nums, target)
    result = get_exp_value_pairs(nums)
    for exp in result:
        if result[exp] == target:
            print(exp)
    print('done')


def get_exp_value_pairs(nums):
    if len(nums) == 1:
        return {str(nums[0]): nums[0]}

    result = {}
    for left in range(1, len(nums)):
        for l_nums in itertools.combinations(nums, left):
            r_nums = nums.copy()
            for e in l_nums:
                r_nums.remove(e)

            l_result = get_exp_value_pairs(list(l_nums))
            r_result = get_exp_value_pairs(r_nums)

            for l_exp in l_result:
                l_val = l_result[l_exp]
                for r_exp in r_result:
                    r_val = r_result[r_exp]
                    result['(%s + %s)' % (l_exp, r_exp)] = l_val + r_val
                    result['(%s - %s)' % (l_exp, r_exp)] = l_val - r_val
                    result['(%s - %s)' % (r_exp, l_exp)] = r_val - l_val
                    result['(%s / %s)' % (l_exp, r_exp)] = l_val * r_val
                    if r_val != 0:
                        result['(%s / %s)' % (l_exp, r_exp)] = l_val / r_val
                    if l_val != 0:
                        result['(%s / %s)' % (r_exp, l_exp)] = r_val / l_val
    return result


if __name__ == '__main__':
    numbers = np.random.randint(1, 14, [4])
    make_num(list(numbers), 24)
    make_num([1, 2, 3, 4], 24)
