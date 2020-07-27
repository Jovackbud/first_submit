nums = [1, 3, 4, 4, 2, 7, 6, 7, 1, 1, 5, 2, 2, 4, 2, 1, 5, 4, 5]
nums_dict = {}

for num in nums:
    if num in nums_dict:
        nums_dict[num] += 1
    else:
        nums_dict[num] = 1

print(nums_dict)
