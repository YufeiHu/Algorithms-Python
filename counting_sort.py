def counting_sort(nums):
    """
    counting sort algorithm's complexity is:
    time = O(n + k)
    space = O(n + k)
    where k = max(nums)
    Apply this algorithm when O(k) <= O(n), and when all numbers in nums are >= 0
    """
    # get frequency list
    num_max = max(nums)
    freqs = [0] * (num_max + 1)
    for num in nums:
        freqs[num] += 1

    # get sumfreqs
    sumfreqs = [0] * (num_max + 1)
    for i in range(1, len(sumfreqs)):
        sumfreqs[i] = freqs[i] + sumfreqs[i-1]

    # get the sorted list
    ans = [0] * len(nums)
    for num in nums[::-1]:
        ans[sumfreqs[num] - 1] = num
        sumfreqs[num] -= 1
    return ans


if __name__ == "__main__":
    nums = [1, 1, 4, 2, 1, 3]
    print(counting_sort(nums))
