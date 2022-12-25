from typing import List
class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        length = len(nums)
        sum2 = {}
        for i in range(length):
            for j in range(i + 1, length):
                tempij = nums[i] + nums[j]
                if tempij not in sum2:
                    sum2[tempij] = []
                sum2[tempij].append((i, j))
        sum2 = sorted(sum2.items(), key=lambda x: x[0])

        res = set()
        left = 0
        right = len(sum2) - 1
        while (left <= right):
            total = sum2[left][0] + sum2[right][0]
            if total == target:
                for i in range(len(sum2[left][1])):
                    for j in range(len(sum2[right][1])):
                        a, b = sum2[left][1][i]
                        c, d = sum2[right][1][j]
                        items = set([a, b, c, d])
                        if len(items) == 4:
                            newItem = [nums[z] for z in items]
                            newItem = tuple(sorted(newItem))
                            res.add((newItem))
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

        result = []
        for item in res:
            result.append([i for i in item])
        return result






