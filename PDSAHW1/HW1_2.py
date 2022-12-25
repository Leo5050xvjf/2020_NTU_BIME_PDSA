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
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue

            left = i+1
            right = length-1
            while left < right:
                temp = nums[i]+nums[left]+nums[right]

                if temp > 0:
                    right -= 1
                elif temp < 0 :
                    left += 1
                else:
                    final_ans.append([nums[i],nums[left],nums[right]])
                    # while left+1 < right and nums[left] == nums[left+1]:
                    #     left += 1
                    # left+=1
                    # while right-1 > left and nums[right] == nums[right-1]:
                    #     right -= 1
                    # right -= 1
                    break

        return final_ans




























