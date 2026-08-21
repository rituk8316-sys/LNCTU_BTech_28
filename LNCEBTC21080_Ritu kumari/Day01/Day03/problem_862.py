# LeetCode 862.Shortest Subarray with Sum at Least K
# solution


from collections import deque

def shortestSubarray(nums, k):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    dq = deque()
    answer = len(nums) + 1

    for i in range(len(prefix)):

        while dq and prefix[i] - prefix[dq[0]] >= k:
            answer = min(answer, i - dq.popleft())

        while dq and prefix[i] <= prefix[dq[-1]]:
            dq.pop()

        dq.append(i)

    if answer <= len(nums):
        return answer
    return -1


# Example
# nums = [2, -1, 2]
# k = 3
# output:3
