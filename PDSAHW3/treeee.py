

from typing import List
class Warriors:
    def warriors(self, strength :List[int], attack_range :List[int]):
        left_stack = [0]
        left_ans = [0]
        right_stack = [len(strength)-1]
        right_ans = [len(strength)-1]


        # print(sol.warriors([1,2,3,],
        #                    [9,8,7,]))
        for left_position in range(1,len(strength)):
            while len(left_stack)!= 0 and strength[left_stack[-1]] < strength[left_position]:
                left_stack.pop()
            if len(left_stack) == 0:
                final_left = max(0,left_position-attack_range[left_position])
                left_ans.append(final_left)
                left_stack.append(left_position)
            else:
                final_left = max(left_stack[-1]+1,left_position-attack_range[left_position])
                left_ans.append(final_left)
                left_stack.append(left_position)


        # print(sol.warriors([11, 13, 11, 7, 15],
        #                    [1, 8,   1,   7,  2]))
        for right_position in range(len(strength)-2,-1,-1):
            while len(right_stack) != 0 and strength[right_stack[-1]] < strength[right_position]:
                right_stack.pop()
            if len(right_stack) == 0:
                final_right = min(len(strength)-1,right_position + attack_range[right_position])
                right_ans.append(final_right)
                right_stack.append(right_position)
            else:
                final_right = min(right_stack[-1]-1,right_position+attack_range[right_position])
                right_ans.append(final_right)
                right_stack.append(right_position)


        right_ans.reverse()
        ans = []
        for left_and_right in range(len(strength)):
            ans.append(left_ans[left_and_right])
            ans.append(right_ans[left_and_right])
        return ans

if __name__ == "__main__":

    if __name__ == "__main__":
        sol = Warriors()
        # print(sol.warriors([1,2,3,4,5],
        #                    [5,4,3,2,1]))
        print(sol.warriors([11, 13, 11, 7, 15],
                           [1, 8, 1, 7, 2]))
        """
        # Output
        [0, 0, 0, 3, 2, 3, 3, 3, 2, 4]
        """