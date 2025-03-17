## sorted
'''
nums = [5, 2, 9, 1, 7, 8, 4, 3, 6]

sorted_nums = sorted(nums, key=lambda x: (x % 2 == 0, x))  # 偶数优先级高
print(sorted_nums)  
# [1, 3, 5, 7, 9, 2, 4, 6, 8]  （奇数在前，偶数在后）
'''
