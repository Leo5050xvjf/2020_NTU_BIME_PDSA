#
import functools
import random
#
#
# a = [[12,3],[18,34],[18,10],[12,45],[18,10],[8,34]]
# a=  sorted(a, key = lambda x:(int(x[0]),int(x[0])))
# print(a)


class Magic:
    def __init__(self,num):
        self.num = num

    def equal(self,object):
        return self.num == object.num

# A = Magic(10)
# B = Magic(10)
# C = Magic(11)
# print(A.equal(B))
# print(A.equal(C))

class Magic:
    def __init__(self,num):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return self.num<other.num
    def __gt__(self, other):
        return self.num > other.num

# A = Magic(10)
# B = Magic(10)
# C = Magic(11)
# # print(A==B)
# # print(A==C)
#
# print(A<B)
# print(A<C)
# print(A>B)
# print(A>C)








# def decoratpor(func):
#     def de():
#         print("now func is : {}".format(func.__name__))
#         func()
#     return de
# def dog():
#     print("林北是狗")
# if __name__ == "__main__":
#     decoratpor(dog)()

# 上述的例子就像是，你覺得dog()這個函數還有東西可以加強或補充，或你還想要他多點什麼
# （只是特殊時用到，因若每次都會常用到就改dog()就好拉，或是說decorator(),對於很多情況都可以最修改、裝飾）
# 因此 ，把dog傳入decorator()，再用de修改成自己想要表達的，再把de return 回來（記住 de()和de是不同東西，de()是一個真的在執行的函式而de只是這個函式的位址）
# 最後decorator(dog)->是de
# 因此要再加上()函式才會真的執行。



# class TT:
#     def __init__(self,id,weight):
#         self.record = []
#         self.weight =weight
#         self.id = id
#
#     def test(self,a,b):
#         self.record.append([a,b])
#
#
# a = TT(1,2)
# a.test(1,2)
# a.test(2,3)
# print(a.record)
# a.test(3,4)
# print(a.record)
#
# a= [1,1,2,2,2,3,4,5,6,6,6,7,7,7,7]
# dict1 = {}
# counter1 = 0
# len_a = len(a)
# while counter1 <len_a:
#     if a[counter1] not in dict1:
#         last_price = a[counter1]
#         last_pos = counter1
#         counter2 = counter1
#         while counter2+1 < len_a:
#             if a[counter2+1] == a[counter1]:
#                 counter2+=1
#             else:
#                 break
#         dict1[a[counter1]] = [counter1,counter2]
#         counter1 = counter2+1
# def find_price_end_tail(arr):
#     dict1 = {}
#     counter1 = 0
#     len_arr = len(arr)
#     while counter1 < len_arr:
#         if arr[counter1] not in dict1:
#             counter2 = counter1
#             while counter2 + 1 < len_arr:
#                 if arr[counter2 + 1] == arr[counter1]:
#                     counter2 += 1
#                 else:
#                     break
#             dict1[arr[counter1]] = [counter1, counter2]
#             counter1 = counter2 + 1
#     return dict1
# a= [1,1,2,2,2,3,4,5,6,6,6,7,7,7,7]
# ans = find_price_end_tail(a)
# print(ans)


# def binart_search(arr,min_,max_):find_price_end_tail




# def binary_search_nearst_min(arr,low,high,x):
#     # Check base case
#     if high >= low:
#
#         mid = (high + low) // 2
#
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
#
#             # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search_nearst_min(arr, low, mid - 1, x)
#
#             # Else the element can only be present in right subarray
#         else:
#             return binary_search_nearst_min(arr, mid + 1, high, x)
#
#     else:
#         # Element is not present in the array
#         return -1
#
#
#
# ans = binary_search_nearst_min(a,0,len(a),96)
# print(ans)

# def binary_search_nearst_min(arr,low,high,x):
#     # Check base case
#     # print("High :", high, "Low :", low)
#     a_min = min(arr)
#     a_max = max(arr)
#     if x<= a_min:
#         return 0
#     elif x>= a_max:
#         return len(arr)-1
#
#
#     if high >= low:
#
#         mid = (high + low) // 2
#         # print(mid)
#         # input()
#
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
#             # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             if mid-1 >=0:
#                 if arr[mid-1] <x:
#                     return mid
#                 elif arr[mid-1] == x:
#                     return mid-1
#
#                 elif arr[mid-1] >x:
#                     if (mid-1-low)+1 > 2:
#                         return binary_search_nearst_min(arr, low, mid - 1, x)
#                     else:
#                         return mid-1
#             # else:
#
#
#
#
#
#             # Else the element can only be present in right subarray
#         elif arr[mid] < x:
#             if mid+1 <=len(a):
#                 if arr[mid+1] <x:
#                     return binary_search_nearst_min(arr, mid + 1, high, x)
#                 elif arr[mid+1] == x:
#                     return mid+1
#                 elif arr[mid+1] >x:
#                     return mid+1
#     else:
#         return None

# a = [13, 23, 42, 52, 53, 58, 72, 73, 79, 87, 96]
# print(a[0:2])
# ans = binary_search_nearst_min(a,0,len(a),10000)
# print(ans)

# def binary_search_nearst_max(arr,low,high,x):
#     # Check base case
#     # print("High :", high, "Low :", low)
#     a_min = min(arr)
#     a_max = max(arr)
#     if x<= a_min:
#         return -1
#     elif x>= a_max:
#         return len(arr)-1
#     elif high >= low:
#         mid = (high + low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             if mid-1 >=0:
#                 if arr[mid-1] <x:
#                     return mid-1
#                 elif arr[mid-1] == x:
#                     return mid-1
#                 elif arr[mid-1] >x:
#                     if (mid-1-low)+1 > 2:
#                         return binary_search_nearst_max(arr, low, mid - 1, x)
#                     else:
#                         return mid-1
#         elif arr[mid] < x:
#             if mid+1 <=len(arr)-1:
#                 if arr[mid+1] <x:
#                     return binary_search_nearst_max(arr, mid + 1, high, x)
#                 elif arr[mid+1] == x:
#                     return mid+1
#                 elif arr[mid+1] >x:
#                     return mid
#     else:
#         return None
# a= [13, 23, 42, 52, 53, 58, 72, 73, 79, 87, 96]
# ans = binary_search_nearst_max(a,0,len(a)-1,1000000)
# if ans == -1:
#     print("沒冬戲")
# print(ans)

class Apple:
    def __init__(self,id):
        self.id = id
        self.list1 = []

    def test(self):
        for i in range(10):
            self.list1.append(i)
A = Apple(10)
A.test()
print(A.list1)




