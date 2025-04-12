# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []

# def solution(nums):
#     if nums == None:
#         return print([])
#     print(sorted(nums)) 

# # solution(None)
def my_sorted(nums):
    for i in range(len(nums) - 1):  
        for j in range(len(nums) - 1):  
            if nums[j] > nums[j + 1]:
                nums[j],nums[j + 1] = nums[j + 1],nums[j]
    return nums


# def solution(nums):

    
#     print (my_sorted(nums) if isinstance(nums, list) else [])

# solution([1,10,3,2,5])


import time

nums = list(range(1000, 0, -1))  # список из 1000 элементов в обратном порядке

# Время для твоей функции
start = time.time()
my_sorted(nums.copy())
time_1 = time.time() - start
print("my_sorted:",time_1)

# Время для встроенной sorted
start = time.time()
sorted(nums)
time_2 = time.time() - start
print("sorted:", time_2)

if time_1 > time_2:
    print(True) 