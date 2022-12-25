from typing import List

class BoardGame:
    def __init__(self, h: int, w: int):
        # stone type
        self.grid = {}
        self.root_table = {}
        self.length_table = {}
        self.h = h
        self.w = w
        # stone length
    def find_root(self,pos):
        while pos != self.root_table[pos]:
            self.root_table[pos] = self.root_table[self.root_table[pos]]
            pos = self.root_table[pos]
        return pos
    def find_pos_O_X_air(self,i,j,stonetype):
        # 上下左右中'O'有幾個
        O_num = 0
        # 'O'在哪
        O_pos = []
        # 'O'的root 和對應的 長度
        O_root_list=  []
        O_length = 0
        X_num = 0
        X_pos = []
        X_root_list=  []
        X_length = 0
        air = 4
        # 可訪問上
        if i >= 1:
            up = (i-1) * self.w + j
            if up in self.grid:
                if self.grid[up] == stonetype:
                    O_num+=1
                    air-=1
                    O_pos.append(up)
                    root = self.find_root(up)
                    if root not in O_root_list:
                        O_root_list.append(root)
                        O_length += self.length_table[root]
                else:
                    air-=1
                    root = self.find_root(up)
                    self.length_table[root] -=1
        # 可訪問下
        if i < self.h-1:
            down = (i+1)*self.w+j
            if down in self.grid:
                if self.grid[down] == stonetype:
                    O_num+=1
                    air-=1
                    O_pos.append(down)
                    root = self.find_root(down)
                    if root not in O_root_list:
                        O_root_list.append(root)
                        O_length+=self.length_table[root]

                else:
                    air -= 1
                    root = self.find_root(down)
                    self.length_table[root] -= 1
        # 訪問左邊
        if j>=1:
            left = i*self.w+j-1
            if left in self.grid:
                if self.grid[left] == stonetype:
                    O_num+=1
                    air-=1
                    O_pos.append(left)
                    root = self.find_root(left)
                    if root not in O_root_list:
                        O_root_list.append(root)
                        O_length += self.length_table[root]
                else:
                    air -= 1
                    root = self.find_root(left)
                    self.length_table[root] -= 1

        if j+1 <= self.w-1:
            right = i * self.w + j + 1
            if right in self.grid:
                if self.grid[right ] ==stonetype:
                    O_num+=1
                    air-=1
                    O_pos.append(right)
                    root = self.find_root(right)
                    if root not in O_root_list:
                        O_root_list.append(root)
                        O_length += self.length_table[root]
                else:
                    air -= 1
                    root = self.find_root(right)
                    self.length_table[root] -= 1

        return O_num,O_pos,O_root_list,O_length,air

    def putStone(self, x: List[int], y: List[int], stoneType: str):
        # open同時，要去考慮周圍相鄰的棋子的周長
        for pos in zip(x,y):
            position = pos[0]*self.w + pos[1]
            self.grid[position] = stoneType
            self.root_table[position] = position
            # self.length_table[position] = 4
            O_num,O_pos,O_root_list,O_length,air = self.find_pos_O_X_air(pos[0],pos[1],stoneType)
            self.length_table[position] = air
            if O_pos :
                O_root_list.append(pos[0]*self.w +pos[1])
                min_root =min(O_root_list)
                final_O_length = O_length + air -O_num

                all_pos = O_root_list + O_pos
                for root in all_pos:
                    self.root_table[root] = min_root
                self.length_table[min_root] = final_O_length

    def surrounded(self, x: int, y: int) -> bool:

        if x*self.w + y in self.grid:
            root = self.find_root(x*self.w+y)
            return self.length_table[root] == 0
        return False

    def getStoneType(self, x: int, y: int) -> str:
        if self.grid[x*self.w+y] == 'O':
            return 'O'
        stoneType = 'X'
        return stoneType




# g = BoardGame(4,4)
#
# g.putStone([1],[1],'X')
# print("g.length_table")
# print(g.length_table)
# g.putStone([1],[2],'O')
# print("g.length_table")
# print(g.length_table)
# g.putStone([2],[1],'O')
# print("g.length_table")
# print(g.length_table)
#
# g.putStone([2],[2],'X')
# print("g.length_table")
# print(g.length_table)
#
# g.putStone([0],[1],'O')
# print("g.length_table")
# print(g.length_table)
# g.putStone([0],[2],'X')
# print("g.length_table")
# print(g.length_table)
# # g.putStone([0],[3],'X')
# # g.putStone([0],[0],'X')
# g.putStone([1],[0],'O')
# print("g.length_table")
# print(g.length_table)
# g.putStone([2],[0],'X')
# print("g.length_table")
# print(g.length_table)
# # g.putStone([3],[0],'X')
# g.putStone([3],[1],'X')
# print("g.length_table")
# print(g.length_table)
# g.putStone([3],[2],'O')
# print("g.length_table")
# print(g.length_table)
# g.putStone([1],[3],'X')
# print("g.length_table")
# print(g.length_table)
# g.putStone([2],[3],'O')
# print("g.length_table")
# print(g.length_table)
# # g.putStone([3],[3],'X')
# print(g.surrounded(2,1))
# print(g.surrounded(1,1))
# print(g.surrounded(1,2))
# print(g.surrounded(2,2))
#
#
# # g = BoardGame(4,4)
# # g.putStone([1],[1],'X')
# # g.putStone([2],[2],'X')
# # g.putStone([0],[1],'O')
# # g.putStone([1],[0],'O')
# # g.putStone([1],[2],'O')
# # g.putStone([2],[1],'O')
# # g.putStone([3],[2],'O')
# # g.putStone([2],[3],'O')
# #
# # print(g.surrounded(1,1))
# # print(g.surrounded(2,2))
# print("g.length_table")
# print(g.length_table)


g = BoardGame(3, 3)
g.putStone([1], [1], 'O')
print(g.surrounded(1, 1))

g.putStone([0, 1, 1], [1, 0, 2], 'X')
print(g.surrounded(1, 1))

g.putStone([2], [1], 'X')
print(g.surrounded(1, 1))
print(g.surrounded(2, 1))

g.putStone([2], [0], 'O')
print(g.surrounded(2, 0))












