

#
a = {}
a[2] = []
print(a)
a[2].append((1,2))
print(a)
a[1] = [(10,9)]
print(a)
sum2 = a
print(sum2.items())
sum2 = sorted(sum2.items(), key=lambda x: x[0])
print(sum2)
# print(sum2.items())

a = {"-9":[-1,-4],"-8":[(-5,-3)]}
sum2 = sorted(a.items(),key = lambda  x : x[0])
print(sum2)
print(sum2[0][0])


# ans = set()
# #
# # ans.add(10)
# # ans.add(1)
# # ans.add(9)
# # ans.add(199)
# # print(ans)
# ans = set([3,2,1,4])
# print(ans)