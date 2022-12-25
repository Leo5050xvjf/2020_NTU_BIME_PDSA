import functools
from typing import List
import random


'''
本版和第二版的差別，是查找min_max_price的對應位置時，是用binary_search，先前是使用while loop，
兩個的差別是，binary search 最差不過就log(N)
而while loop 雖然直觀好寫，但worse case 是 O(N)的時間
在大量資料使用Filter時，兩者的差距會越來越大

'''
class Restaurant(object):
    def __init__(self, id: int, rate: int, price: int, distance: int):
        self.id = id
        self.rate = rate
        self.price = price
        self.distance =distance


    def getID(self) -> int:
        return self.id
    def __lt__(self, b) -> bool:
        return (self.distance*self.price)/self.rate < (b.distance*b.price) / b.rate

    @staticmethod
    def comparator1(a, b) -> int:
        if a.rate < b.rate:return -1
        elif a.rate == b.rate:
            if a.distance < b.distance:return -1
            elif a.distance == b.distance:
                if a.id<b.id:return 1
                elif a.id == b.id:return 0
                return -1
            return 1
        return 1
    @staticmethod
    def comparator2(a,b):
        if a.distance<b.distance:return -1
        elif a.distance>b.distance:return 1
        else:
            if a.id > b.id:return -1
            elif a.id < b.id: return 1
            return 0

    @staticmethod
    def comparator3(a,b):
        return a.price-b.price

class Restaurants(object):
    def __init__(self, restaurants: List[Restaurant]):
        # 以price排好的list
        self.price_order_restaurants =sorted(restaurants,key = functools.cmp_to_key(Restaurant.comparator3))
        # 建立一個字典{price:[position_head,position_end]},和一個 單純只有price的list(因為我不知道如何把binary search 用在字典裡，我只會用在list裡面)
        self.price_list,self.price_dict = self.find_price_end_tail(self.price_order_restaurants)
        self.price_list_low = 0
        self.price_list_high = len(self.price_list)-1
        self.minimum_price =min(self.price_dict)
        self.maximum_price = max(self.price_dict)


    # 先找出每個price對應的起點和終點
    def find_price_end_tail(self,arr):
        dict1 = {}
        price_list = []
        counter1 = 0
        len_arr = len(arr)
        while counter1 < len_arr:
            if arr[counter1].price not in dict1:
                price_list.append(arr[counter1].price)
                counter2 = counter1
                while counter2 + 1 < len_arr:
                    if arr[counter2 + 1].price == arr[counter1].price:
                        counter2 += 1
                    else:break
                dict1[arr[counter1].price] = [counter1, counter2]
                counter1 = counter2 + 1

        # 已找到head and tail
        return price_list,dict1
    # 用binary_search,找到離min_prcie最近且“合法”的price的位置，例如:[2,5,6] 若min_price是3 ，則回傳5的位置
    def binary_search_nearst_min(self,arr, low, high, x):
        # Check base case

        if x <= self.minimum_price:return 0
        elif x > self.maximum_price:return -1
        elif high >= low:
            mid = (high + low) // 2

            if arr[mid] == x:return mid
            elif arr[mid] > x:
                if mid  > 0:
                    if arr[mid - 1] < x:return mid
                    elif arr[mid - 1] == x:return mid - 1

                    elif arr[mid - 1] > x:
                        if mid-low > 2:return self.binary_search_nearst_min(arr, low, mid - 1, x)
                        else:return mid - 1
            elif arr[mid] < x:
                if mid  <= self.price_list_high:
                    if arr[mid + 1] < x:return self.binary_search_nearst_min(arr, mid + 1, high, x)
                    elif arr[mid + 1] == x:return mid + 1
                    elif arr[mid + 1] > x:return mid + 1
    # 和binary_search_nearst_min概念差不多
    def binary_search_nearst_max(self,arr, low, high, x):

        if x < self.minimum_price:return -1
        elif x >= self.maximum_price:return self.price_list_high
        elif high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:return mid
            elif arr[mid] > x:
                if mid - 1 >= 0:
                    if arr[mid - 1] < x:return mid - 1
                    elif arr[mid - 1] == x:return mid - 1
                    elif arr[mid - 1] > x:
                        if mid-low > 2:return self.binary_search_nearst_max(arr, low, mid - 1, x)
                        else:return mid - 1
            elif arr[mid] < x:
                if mid + 2 <= len(arr):
                    if arr[mid + 1] < x:return self.binary_search_nearst_max(arr, mid + 1, high, x)
                    elif arr[mid + 1] == x:return mid + 1
                    elif arr[mid + 1] > x:return mid
    def filter(self, min_price: int, max_price: int, min_rate: int):
        ans = []
        min_price_position =self.binary_search_nearst_min(self.price_list,0,self.price_list_high,min_price)
        max_price_position = self.binary_search_nearst_max(self.price_list,0,self.price_list_high,max_price)
        # 判斷特例，若min max price不在 price_list 裡面 直接回傳-1
        if min_price_position ==-1 or max_price_position == -1:
            return ans
        min_price_true_pos =self.price_dict[self.price_list[min_price_position]][0]
        max_price_true_pos = self.price_dict[self.price_list[max_price_position]][1]

        ans = [restaurant for restaurant in self.price_order_restaurants[min_price_true_pos:max_price_true_pos+1] if restaurant.price<=max_price and restaurant.rate >= min_rate ]
        if not ans:return ans
        return [restaurant.id for restaurant in sorted(ans,key=functools.cmp_to_key(Restaurant.comparator2))]




































