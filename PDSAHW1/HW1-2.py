from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        final_ans = []
        nums = sorted(nums)
        for i in range(length-2):
            if nums[i] + nums[i+2] + nums[i+1] > 0:
                break
            if nums[i] + nums[length-2] + nums[length-1] < 0:
                continue
            left = i+1
            right = length-1
            while left < right:
                temp = nums[i]+nums[left]+nums[right]

                if temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    final_ans.append([nums[i], nums[left], nums[right]])
                    left,right  = left+1,right-1
        return final_ans



a = [-89541368, -31794286, 34018216, 87317438]
print(sum(a))




