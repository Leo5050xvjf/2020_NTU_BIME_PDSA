import functools
from typing import List
import random


'''此版是建立{price:position}的字典，但時間超過
   猜測可改善地方：1.如果min_price不在字典裡，不要用回圈去慢慢找是否有符合的選項，這樣的woese case 是 O(N)

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
            if a.id < b.id: return 1
            return 0


class Restaurants(object):
    def __init__(self, restaurants: List[Restaurant]):
        # 以price排好的list
        self.price_order_restaurants =sorted(restaurants,key = functools.cmp_to_key(lambda x,y:x.price-y.price))
        # 建立一個字典{position : price}
        self.price_dict = self.find_price_pos(self.price_order_restaurants)
        self.record = {}
    # 找到每個price的起始位置，例如：{5:0,6:1,7:10}->意思是說 5元在self.price_order_restaurants的0號位置
    # 回傳一個字典
    def find_price_pos(self,arr):
        price_dict = {}
        counter = 0
        for restaurant in arr:
            if restaurant.price not in price_dict:
                price_dict[restaurant.price] = counter
            counter+=1
        return price_dict
    # 當filter輸入min_price,max_price時，找到符合的min_price位置，因為filter輸入的不一定在列表裡面，因此從輸入的min_price開始往max_price找符合的值（都是整數）
    def find_price_dict_pos(self,price_dict,min_,max_):
        # maybe binary_search
        while min_ not in price_dict:
            min_ += 1
            if min_ > max_:return None
        return min_

    def filter(self, min_price: int, max_price: int, min_rate: int):
        ans = []
        if min_price not in self.record:
            min_ = self.find_price_dict_pos(self.price_dict, min_price, max_price)
            if min_ is None:
                return []
            self.record[min_price] = min_
            min_pos = self.price_dict[min_]
            for restaurant in self.price_order_restaurants[min_pos:]:
                if restaurant.price<=max_price and restaurant.rate >= min_rate:
                    ans.append(restaurant)
                elif restaurant.price > max_price:
                    break
            #return的是一個充滿restaurant的list
            if not ans:return ans
            ans = sorted(ans,key=functools.cmp_to_key(Restaurant.comparator2))
            return [ restaurant.id for restaurant in ans]
        else:
            min_price = self.record[min_price]
            min_pos = self.price_dict[min_price]
            for restaurant in self.price_order_restaurants[min_pos:]:
                if restaurant.price<=max_price and restaurant.rate >= min_rate:
                    ans.append(restaurant)
                elif restaurant.price > max_price:
                    break
            #return的是一個充滿restaurant的list
            if not ans:return ans
            ans = sorted(ans,key=functools.cmp_to_key(Restaurant.comparator2))
            return [ restaurant.id for restaurant in ans]

    def print_res(self, arr):
        for restaurant in arr:
            print("Restaurant :", [restaurant.id, restaurant.rate, restaurant.price, restaurant.distance
                                   ])

if __name__ == "__main__":
    rests = [
        # id, rate, price, distance

        Restaurant(19, 4, 19, 12),
        Restaurant(15, 3, 19, 11),
        Restaurant(18, 5, 20, 11),
        Restaurant(20, 1, 20, 12),



    ]
    r = Restaurants(rests)
    # arr = r.find_price_pos(r.price_order_restaurants)
    # r.print_res(r.price_order_restaurants)
    # print(arr)
    print(r.filter(0, 25, 3))
    print(r.filter(0, 25, 4))

    print(r.filter(0, 10, 1))
    print(r.filter(0, 19, 1))
    print(r.filter(19, 19, 3))
    print(r.filter(0, 20, 1))
    # print(r.get_first_filter_increase_order_price_list(0, 25, 3))
    # print(r.get_first_filter_increase_order_price_list(0, 25, 4))
    # print(r.get_first_filter_increase_order_price_list(0, 10, 1))
    # print(r.get_first_filter_increase_order_price_list(0, 19, 1))
    # print(r.get_first_filter_increase_order_price_list(19, 19, 3))
    # print(r.get_first_filter_increase_order_price_list(0, 20, 1))
    #
    # print(r.get_first_filter_increase_order_price_list(0, 19, 1))
    # print(r.get_first_filter_increase_order_price_list(19, 19, 3))

    #
    # # case6
    # rests = [
    #     # id, rate, price, distance
    #     Restaurant(3, 2, 3, 8),
    #     Restaurant(0, 2, 4, 6),
    #     Restaurant(2, 4, 5, 12),
    #     Restaurant(1, 5, 6, 11),
    # ]
    # print([i.getID() for i in sorted(rests)])
    # print([i.getID() for i in sorted(rests, key=functools.cmp_to_key(Restaurant.comparator1))])
#[18, 15, 19]
# [18, 19]
# []
# [15, 19]
# [15, 19]
# [18, 15, 20, 19]
