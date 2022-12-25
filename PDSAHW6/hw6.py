from typing import List


'''

先前字典的寫法，無法預防node分群突然連結起來的情況（事實上應該要先把所有點的關係建立起來就可以了）
例如: [0,1],[2,3],[1,3] 會因為node建立順序造成答案有問題

Ans :用BFS 或 DFS 可以避免這個問題,且須先把所有點的關係建立起來（也就是把每個點對應的鄰點找出來）
每個群的相鄰node顏色需不同（node群可以複數個, 例如：[0,1],[2,3]）
'''


class Teams:
    def teams(self, idols: int, teetee: List[List[int]]) -> bool:
        status_dict = {}
        '''
        status_dict-> {0:[1,-1],2:[0,0]} 
        key = node :  value = [node的狀態,node的顏色]
        '''
        adj_dict = {}
        '''
        
        {
        1:[與1相連的所有node]
        3:[與3相連的所有node]
        .
        .
        .}
        
        '''
        # 先建立adjacency list
        for pair in teetee:

            if pair[0] in adj_dict and pair[1] in adj_dict:
                adj_dict[pair[0]].append(pair[1])
                adj_dict[pair[1]].append(pair[0])
            elif pair[0] in adj_dict and pair[1] not in adj_dict:
                adj_dict[pair[0]].append(pair[1])
                adj_dict[pair[1]] = [pair[0]]
                status_dict[pair[1]] = [0,0]
            elif pair[0] not in adj_dict and pair[1] in adj_dict:
                adj_dict[pair[0]] = [pair[1]]
                adj_dict[pair[1]].append(pair[0])

                status_dict[pair[0]] = [0,0]

            elif pair[0] not in adj_dict and pair[1] not in adj_dict:
                adj_dict[pair[0]] = [pair[1]]
                adj_dict[pair[1]] = [pair[0]]
                status_dict[pair[0]] = [0,0]
                status_dict[pair[1]] = [0,0]


        #做DFS
        def dfs(node,color = -1):
            status_dict[node] = [1,color]
            q = []
            for _ in adj_dict[node]:
                if status_dict[_][0] == 0:
                    status_dict[_][0] = 1
                    status_dict[_][1] = -color
                    q.append(_)
                else:
                    if status_dict[_][1] == color:
                        return False
            while len(q) > 0:
                node = q.pop(0)
                c= status_dict[node][1]
                for _ in adj_dict[node]:
                    if status_dict[_][0] == 1:
                        if status_dict[_][1] == c:
                            return False
                    else:
                        status_dict[_] = [1,-c]
                        q.append(_)
        #把adj_list 遍歷一遍
        for k,v in adj_dict.items():
            if status_dict[k][0] == 0:
                s = dfs(k)
            if s == False:
                return False
        return True


if __name__ == "__main__":
    # example 1: True
    print(Teams().teams(4, [[0,1],[0,3],[2,1],[3,2]]))
    # example 1: False
    print(Teams().teams(4, [[0,1],[0,3],[0,2],[2,1],[3,2]]))

    print(Teams().teams(3, [[0, 1], [3,2], [2,1]]))

    print(Teams().teams(3, [[0, 1], [0,2], [3,0],[4,5]]))

    print(Teams().teams(4, [[1,2],[2,3],[4,5,],[1,3]]))