
class Percolation:

    def __init__(self, N: int):
        """ Create N-by-N grid, with all sites blocked """
        '''作業的(i , j)對應的就是圖片的座標，兩個一樣，因此要對應至arr的位置，需要
            (i , j )->i*N + j ex:3*3的grid，則(1,1)->1*3 + 1 = 4 所以在arr[4]的位置                       '''
        self.N = N
        self.arr = [-1 for i in range(N*N)]
        self.down_row = []
        self.have_percolated = False

    def find_root(self,index):
        while index != self.arr[index]:
            self.arr[index] = self.arr[self.arr[index]]
            index = self.arr[index]
        return index

    def open(self, i: int, j: int):
        """ Open site (row i, column j) if it is not open already """
        arr_pos = i * self.N + j
        if i == self.N-1:
            self.down_row.append(arr_pos)
        pos_list_root = [arr_pos]
        # 如果i,j上方的座標點，是合法的位置，且他已經open的話，則紀錄他的位置
        if i >= 1:
            arr_pos_up = arr_pos - self.N
            if self.arr[arr_pos_up] != -1:
                pos_list_root.append(arr_pos_up)
                pos_list_root.append(self.find_root(arr_pos_up))

        if j >= 1:
            arr_pos_left = arr_pos - 1
            if self.arr[arr_pos_left] != -1:
                pos_list_root.append(arr_pos_left)
                pos_list_root.append(self.find_root(arr_pos_left))
        if j < self.N-1:
            arr_pos_right = arr_pos + 1
            if self.arr[arr_pos_right] != -1:
                pos_list_root.append(arr_pos_right)
                pos_list_root.append(self.find_root(arr_pos_right))
        if i < self.N-1:
            arr_pos_down = arr_pos + self.N
            if self.arr[arr_pos_down] != -1:
                pos_list_root.append(arr_pos_down)
                pos_list_root.append(self.find_root(arr_pos_down))
        min_root = min(pos_list_root)
        for root_pos in pos_list_root:
            self.arr[root_pos] = min_root

    def isOpen(self, i: int, j: int) -> bool:
        """ Is site (row i, column j) open? """
        if self.arr[i*self.N + j] == -1:
            return False
        return True

    def isFull(self, i: int, j: int) -> bool:
        """ Is site (row i, column j) full? """
        if i * self.N + j < self.N:
            return True
        index = self.find_root(i * self.N + j)
        return 0 <= index < self.N


    def percolates(self) -> bool:
        """ Does the system percolate? """
        if not self.have_percolated:
            for down_row_pos in self.down_row:
                index = self.find_root(down_row_pos)
                if 0<= index <self.N:
                    self.have_percolated =True
                    return True
            return False
        return True






