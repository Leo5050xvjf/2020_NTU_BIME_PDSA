from typing import List
import heapq
# import numpy

class Mountains:
    def mountains(self, mountains_height: List[List[int]]) -> int:
        n= len(mountains_height)
        m =len(mountains_height[0])
        # [目前累積高度,自己的位置(1d)]
        heap = []
        visited = [-1 for _ in range(n * m)]
        cum_weight = [float("Inf") for _ in range(n * m)]
        previous_node = [(-1,-1) for _ in range(n * m)]
        h=  lambda x,y : x-y if (x-y)>0 else 2 * (y-x)
        one_d = lambda x,y,m :x*m + y


#       初始化起點

        def legel_pos(x,y,n,m):
            candidate = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            ans = []
            for _ in candidate:
                # 上下左右
                if (_[0] < 0 or _[0] > n-1 or _[1] < 0 or _[1] > m-1): continue
                if visited[_[0] * m + _[1]] == 1: continue
                ans.append(_)
            return ans
        visited[0] = 1
        cum_weight[0] = 0
        previous_node[0] = (0,0)
        init_list = legel_pos(0,0,n,m)
        height = 0
        for _ in init_list:
            edge_ = h(mountains_height[0][0], mountains_height[_[0]][_[1]])
            if edge_ + height < cum_weight[one_d(_[0], _[1], m)]:

                cum_weight[one_d(_[0], _[1], m)] = edge_ + height
                previous_node[one_d(_[0], _[1], m)] = (0,0)
                heapq.heappush(heap, (edge_ + height, _))

        while visited[n*m-1] != 1 and len(heap) > 0:
            height,pos = heapq.heappop(heap)
            visited[one_d(pos[0],pos[1],m)] = 1
            pos_list = legel_pos(pos[0],pos[1],n,m)
            for _ in pos_list:
                edge_ = h(mountains_height[pos[0]][pos[1]],mountains_height[_[0]][_[1]])
                if edge_+height < cum_weight[one_d(_[0],_[1],m)]:
                    cum_weight[one_d(_[0], _[1], m)] = edge_+height
                    previous_node[one_d(_[0], _[1], m)] = pos
                    heapq.heappush(heap,(edge_+height,_))
        return cum_weight[n * m -1]

if __name__ == "__main__":


    print(Mountains().mountains(
        [[1],
         [2]]))
    print(Mountains().mountains(
        [[ 0, 1, 2, 3, 4],
         [24,23,22,21, 5],
         [12,13,14,15,16],
         [11,17,18,19,20],
         [10, 9, 8, 7, 6]]))
    # ans=42
    print(Mountains().mountains(
        [[10, 11, 5],
         [11, 3, 5]
         ]))

    print(Mountains().mountains(
        [[3, 4, 5],
         [9, 3, 5],
         [7, 4, 3]]))

    # ans=6