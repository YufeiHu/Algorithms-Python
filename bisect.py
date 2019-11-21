def bisect_left(nums, val):
    if not nums:
        return -1
    if val < nums[0]:
        return 0
    if val > nums[-1]:
        return len(nums)

    l = 0
    r = len(nums)
    while True:
        if l + 1 == r:
            if nums[l] == val:
                return l
            else:
                return l + 1
        m = (l + r) // 2
        if val <= nums[m]:
            r = m
        else:
            l = m


def bisect_right(nums, val):
    if not nums:
        return -1
    if val < nums[0]:
        return 0
    if val > nums[-1]:
        return len(nums)

    l = 0
    r = len(nums)
    while True:
        if l + 1 == r:
            return l + 1
        m = (l + r) // 2
        if val < nums[m]:
            r = m
        else:
            l = m


if __name__ == "__main__":
    nums = [0, 0, 1, 4, 4, 5, 6, 7, 8, 10]
    print(bisect_left(nums, 4))
    print(bisect_right(nums, 4))
