
from typing import List
#
class Teams:
    def teams(self, idols: int, teetee: List[List[int]]) -> bool:
        dict_ = {}
        n = len(teetee)

        # print(teetee)
        for pair in teetee:

            status_ = [0,0]
            l_node ,r_node = pair[0],pair[1]
            if l_node not in dict_:
                status_[0] = 1
            if r_node not in dict_:
                status_[1] = 1

            if status_ == [1,1]:
                dict_[l_node] ,dict_[r_node]= -1,1
            elif status_==[1,0]:
                dict_[l_node] = -dict_[r_node]
            elif status_ == [0,1]:
                dict_[r_node] = - dict_[l_node]
            elif status_ == [0,0]:
                if dict_[r_node] == dict_[l_node]:return False
        return True


if __name__ == "__main__":
    # example 1: True
    print(Teams().teams(4, [[0,1],[0,3],[2,1],[3,2]]))
    # example 1: False
    print(Teams().teams(4, [[0,1],[0,3],[0,2],[2,1],[3,2]]))


