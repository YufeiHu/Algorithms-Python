def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m
        else:
            return m
    return -1


if __name__ == "__main__":
    nums = [1, 4, 6, 6, 8, 9, 10, 11, 13, 14]
    print(binary_search(nums, 10))
    
