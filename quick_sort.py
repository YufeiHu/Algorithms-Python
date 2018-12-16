def quick_sort(nums):
    if len(nums) == 0: return nums
    if len(nums) == 1: return nums

    pivot = nums[0]
    left = 1
    for right in range(1, len(nums)):
        if nums[right] < pivot:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    left -= 1
    nums[0], nums[left] = nums[left], nums[0]

    left_ans = quick_sort(nums[:left])
    right_ans = quick_sort(nums[left + 1:])

    return left_ans + [nums[left]] + right_ans


if __name__ == "__main__":
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(nums))
