def merge_sort(nums):
    if len(nums) <= 1: return nums

    a = merge_sort(nums[:len(nums) // 2])
    b = merge_sort(nums[len(nums) // 2:])

    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            i += 1
        else:
            a.insert(i, b[j])
            i += 1
            j += 1

    a.extend(b[j:])
    return a


if __name__ == "__main__":
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(nums))
