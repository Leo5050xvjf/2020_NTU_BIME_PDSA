from typing import List
import heapq

'''
問題解釋：在2D平面上，找出要求的points set，每次合併點都是以最近的兩點做合併，而合併是以形心，不是平均就好。

1.
    a.先初始化一個2D陣列，紀錄著每個點加入heap時的狀態，狀態以當前集合數量表示(集合數量只會變少，初始數量為N)->check_board
    b.接著創建一個大小為N的狀態列表，紀錄該點的狀態，1:表示已經融合，不在平面上。-1:表示此點為某clusters 的形心。0:表示此點未作討論。
    c.創建一個2D的列表，紀錄clusters 形心的X_sum,Y_sum，方便融合時順便計算形心
    d.創建一個2D的列表，紀錄clusters 是由多少個點融合出來的，方便融合時順便計算形心
    e.heap 內，每個node以distance做排序，每個node 包含資訊 ： (distance,[p1_index,p2_index],current_N)
2.
    更新列表，取出heap[0]並加以討論。
    
    若heap[0] node 中，發現相對應的status_有1，則pop()。原因是因為此點已經不存在在平面上，此node 為之前某狀態時留下的關係。
    若heap[0] node 中，發現相對應的status_有-1，則再次確認此node的current_num 是否和 check_board相同
        ->解釋：以下面的語法來說，融合點（cluster）的出現，會更新融合點與其他"存在點"的關係，在更新的同時，因為已發生融合，故整個平面上的clusters 又減少1次
                需要特別補充的是，clusters的狀態如果更新(減少)，代表他一定在上一個操作合併某點，故heap[0]若為-1且 狀態不合，表示此點不能用。
                思考：那這樣會造成答案遺失嗎？
                A:不會，融合後的新clusters 會更新以自己為中心和其他點的關係和狀態。
    若不屬於以上兩種情況，break。->找到合法的min distance node。
    
    得出合法的node，融合後得到新的point形心)，更新上面的初始列表b,c,d
    
    接著以新的形心點為中心，遍歷所有點（其中狀態為1 或 index 和 新融合點相同的 ，則略過）
    更新a的狀態，且把新的點與其他點的關係再放入heap中
    
    重複以上循環 直到達到指定set numbers。


'''

'''
幾個特別的地方
1.若此heap 有一些點一直沉在底部，則此heap 會隨著使用時間越來越大，需要注意。
2.此方法不是最佳的space。
3.取的是形心，不是平均。

4.個人覺得最神奇的操作在check_board(黃大師想的)，且把所有資訊壓在最小的clusters index 身上，類似於root的概念
過程中list大小保持不變，只是把點一直往index小的地方更新，此想法在很多資料結構都有出現，是一個省時省空間的做法（當然需要動腦才比較看得懂）
而狀態[1,0,-1]在很多程式執行上也常出現，我想的:)


'''

class Cluster:
    def cluster(self, points: List[List[int]], cluster_num: int) -> List[List[float]]:
        self.length = len(points)
        distance_heap, check_board, status_ = self.creat_init_(points,self.length)
        return self.update_(points,distance_heap, check_board, status_ ,cluster_num,self.length)
    def creat_init_(self,point_list,length):
        # 初始化一個檢查表、heap、狀態表、
        # heap 裡面是以： (點對點的距離,[p1,p2],Current_N)
        '''
            點對點的距離，準確來說是行心對形心的距離
            [p1,p2]:以p1<p2排序 （p1,p2是points裡面的index）
            此時N的數量：其目的在於，紀錄heap出來的node是否為合法，若為上一個狀態的N(例如：現在為10，則上一個狀態為11)
            則表示，此點已經不合法，因為它屬於上一個狀態的關係
        '''
        check_board= [[0 for _ in range(length)] for __ in range(length)]
        distance_heap = []
        status_ = [0 for _ in range(length)]
        counter = 0
        dis = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        for j,p1 in enumerate(point_list):
            for i,p2 in enumerate(point_list):
                if i>j:
                    check_board[j][i] = length
                    heapq.heappush(distance_heap, (dis(p1, p2), [j,i], length))
        return distance_heap,check_board,status_

    def update_(self,points,distance_heap, check_board, status_,clu_num,length):

        cluster_X_Y_sum = points.copy()
        cluster_check_num =[1 for _ in range(length)]

        dis = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        sum_ = lambda x,y:[(x[0]+y[0]),(x[1]+y[1])]
        # distance_heap:[距離,兩點list,current_N]
        current_N = length
        need_loop_num = length-clu_num
        for _ in range(need_loop_num):
            while True:
                p1_index,p2_index = distance_heap[0][1]
                status_list = [status_[p1_index],status_[p2_index]]
                if 1 in status_list:heapq.heappop(distance_heap)
                elif -1 in status_list:
                    if check_board[p1_index][p2_index] != distance_heap[0][2]:heapq.heappop(distance_heap)
                    else:break
                else:break
            dis_ ,[p1_index,p2_index],recoard_N = heapq.heappop(distance_heap)
            cluster_X_Y_sum[p1_index] = sum_(cluster_X_Y_sum[p1_index],cluster_X_Y_sum[p2_index])
            cluster_check_num[p1_index] = cluster_check_num[p1_index] + cluster_check_num[p2_index]
            # 產生新點並取代原位置
            points[p1_index] = [cluster_X_Y_sum[p1_index][0]/cluster_check_num[p1_index],cluster_X_Y_sum[p1_index][1]/cluster_check_num[p1_index]]
            # 1表示以融合消失，不再討論
            # -1代表被更新，繼續討論
            status_[p1_index] ,status_[p2_index] = -1,1
            '''
            此地方曾經出錯，[p1_index, i] = sorted([p1_index,i]) 應改成 [p1_index_, i_] = sorted([p1_index,i])，因為p1_index是一個核心，不應該在迴圈內變更。
            '''
            for i in range(length):
                if status_[i] != 1 and i != p1_index:
                    [p1_index_, i_] = sorted([p1_index,i])
                    heapq.heappush(distance_heap,(dis(points[p1_index_],points[i_]),[p1_index_,i_],current_N ))
                    check_board[p1_index_][i_] = current_N
            current_N -= 1
            ans = []
        for i,_ in enumerate(status_):
            if _ == -1 or _ == 0:
                ans.append(points[i])
        return sorted(ans)


if __name__ == "__main__":
#
#
    print(Cluster().cluster([[0, 0], [1, 0], [3, 0], [0, 1]], 3))
        # # [[0.3333333333333333, 0.3333333333333333], [3, 0]]
        # # [0,0], [1,0], [0,1] are in same cluster
        # # [3,0] are in another cluster
#         #
#         # print(Cluster().cluster([[0, 3], [3, 3], [4, 7], [9, 0], [9, 4]], 3))
#         # # [[1.5, 3.0], [4, 7], [9.0, 2.0]]
#         #
#         # print(Cluster().cluster([[0, 1], [0, 2], [3, 1], [3, 2]], 2))
#         # [[0.0, 1.5], [3.0, 1.5]]
    print(Cluster().cluster([[5, 9], [8, 4], [6, 3], [6, 9], [8, 3], [4, 7], [7, 2], [6, 6], [6, 1], [2, 2]], 1))
#     # # [[5.8, 4.6]]
#     # # Repeat: False
#     #
#     print(Cluster().cluster([[9, 2], [8, 4], [2, 7], [4, 1], [5, 8], [5, 6], [4, 6], [2, 2], [6, 1], [1, 3]], 2))
#     # [[3.625, 4.25], [8.5, 3.0]]
#     # Repeat: False
#     #
    print(Cluster().cluster([[2, 1], [1, 5], [1, 7], [4, 2], [5, 6], [1, 6], [4, 1], [8, 4], [6, 7], [4, 3]], 2))
#     # # [[1.0, 6.0], [4.714285714285714, 3.4285714285714284]]
#     # # Repeat: False
#     #
#     print(Cluster().cluster([[3, 5], [6, 8], [6, 4], [9, 8], [6, 7], [5, 6], [8, 7], [8, 5], [5, 1], [5, 7]], 4))
#     # # [[3, 5], [5, 1], [6.0, 6.166666666666667], [8.5, 7.5]]
#     # # Repeat: False
#     #
#     print(Cluster().cluster([[4, 3], [8, 2], [2, 1], [7, 9], [4, 5], [8, 3], [3, 6], [9, 3], [5, 5], [7, 8]], 2))
#     # [[5.375, 3.5], [7.0, 8.5]]
#     # Repeat: False
#
#     print(Cluster().cluster([[6, 4], [2, 1], [7, 6], [7, 3], [1, 1], [6, 9], [2, 9], [9, 5], [3, 9], [1, 7]], 3))
#     # [[1.5, 1.0], [3.0, 8.5], [7.25, 4.5]]
#     # Repeat: False
#
#     print(Cluster().cluster([[4, 2], [3, 3], [5, 9], [8, 8], [5, 1], [9, 8], [3, 2], [6, 5], [4, 8], [5, 3]], 3))
#     # [[4.333333333333333, 2.6666666666666665], [4.5, 8.5], [8.5, 8.0]]
#     # Repeat: False
#
#     print(Cluster().cluster([[7, 9], [1, 1], [1, 5], [4, 2], [3, 2], [4, 8], [9, 3], [6, 4], [5, 2], [1, 6]], 4))
#     # [[1.0, 5.5], [3.8, 2.2], [5.5, 8.5], [9, 3]]
#     # Repeat: False














