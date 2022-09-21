# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.
array1 = [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]

array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
# Output:
# [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

def zeros(list):
    num_of_zeros = 0
    new_list = []
    for num in list:
        if num == 0:
            num_of_zeros += 1
        else:
            new_list.append(num)
    while num_of_zeros > 0:
        new_list.append(0)
        num_of_zeros -= 1
    return new_list

print(zeros(array1))
print(zeros(array2))























