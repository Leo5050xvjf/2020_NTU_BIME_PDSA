from typing import List
import heapq


class Railway():
    def __init__(self):
        self.status_dict = {}
        self.adj_dict = {}


    def railway(self, landmarks: int, distance: List[List[int]]) -> int:

        for pair in distance:
            if pair[0] in self.adj_dict and pair[1] in self.adj_dict:
                self.adj_dict[pair[0]].append((pair[2],pair[1]))
                self.adj_dict[pair[1]].append((pair[2],pair[0]))
            elif pair[0] in self.adj_dict and pair[1] not in self.adj_dict:
                self.adj_dict[pair[0]].append((pair[2],pair[1]))
                self.adj_dict[pair[1]] = [(pair[2],pair[0])]
                self.status_dict[pair[1]] = False
            elif pair[0] not in self.adj_dict and pair[1] in self.adj_dict:
                self.adj_dict[pair[0]] = [(pair[2],pair[1])]
                self.adj_dict[pair[1]].append((pair[2],pair[0]))

                self.status_dict[pair[0]] = False

            elif pair[0] not in self.adj_dict and pair[1] not in self.adj_dict:
                self.adj_dict[pair[0]] = [(pair[2],pair[1])]
                self.adj_dict[pair[1]] = [(pair[2],pair[0])]
                self.status_dict[pair[0]] = False
                self.status_dict[pair[1]] = False

        return 0

    # def prim_alg(self,):



if __name__ == "__main__":
    print(
        Railway().railway(4, [[0, 1, 2],
                              [0, 2, 4],
                              [1, 3, 5],
                              [2, 1, 1]])
    )
    # Answer: 8 (2 + 5 + 1)

    print(
        Railway().railway(4, [[0, 1, 0],
                              [0, 2, 4],
                              [0, 3, 4],
                              [1, 2, 1],
                              [1, 3, 4],
                              [2, 3, 2]])
    )
    # Answer: 3(0 + 1 + 2)