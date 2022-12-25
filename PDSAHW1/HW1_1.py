



#
# a =  [1 ,2 ,3 ,5 ,8,1000]
# dict1 = {}
# target = 1001
# location = 0
# def solution(a,dict1,location,target):
#     ans = []
#     for i in a:
#         if i in dict1:
#             ans.append(dict1[i])
#             ans.append(location)
#             # print(dict1[i],location)
#             return ans
#         else:
#             dict1[target - i] = location
#             location+=1
#
# ans  = solution(a,dict1,location,target)
# print("The ans is : ",ans)


import HW1_2
ans = HW1_2.Solution()
a = [-10,-9,-8,0,1,2,3,4,5,6,7,8,9]
Ans = ans.threeSum(a)
print(Ans)


