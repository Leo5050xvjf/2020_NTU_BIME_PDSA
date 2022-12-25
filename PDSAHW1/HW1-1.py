from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        location = 0
        ans = []
        dict1 = {}
        for i in nums:
            if i in dict1:
                ans.append(dict1[i])
                ans.append(location)
                return ans
            else:
                dict1[target - i] = location
                location += 1


