def heap_sort(nums):
    # convert nums to heap
    length = len(nums) - 1
    least_parent = length // 2
    for i in range(least_parent, -1, -1):
        move_down(nums, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if nums[0] > nums[i]:
            swap(nums, 0, i)
            move_down(nums, 0, i - 1)


def move_down(nums, first, last):
    largest = 2 * first + 1
    while largest <= last:

        # right child exists and is larger than left child
        if (largest < last) and (nums[largest] < nums[largest + 1]):
            largest += 1

        # right child is larger than parent
        if nums[largest] > nums[first]:
            swap(nums, largest, first)

            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return


def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


if __name__ == "__main__":
    nums = [20, 6, 3, 56, 711, 2, 5, 64, 1, 2, 2, 2]
    heap_sort(nums)
    print(nums)
