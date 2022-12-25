


strength   = [0,0,10,2,0]
attack_range = [0,2000,1,1,100000]
def stack(strength ,attack_range):
    stack_left = [0]
    left_pos = [0]

    stack_right = [len(strength  )-1]
    right_pos =[len(strength  )-1]

    for position in range(1,len(strength  ) ):
        if strength  [stack_left[-1]] > strength  [position] :
            stack_left.append(position)
            left_pos.append(position)
        elif strength [stack_left[-1]] == strength  [position]:
            stack_left.pop()
            stack_left.append(position)
            left_pos.append(position)
        else:
            find_ans = False
            while len(stack_left) != 0 and strength  [stack_left[-1]] < strength  [position]:
                if ( position-stack_left[-1] ) >= attack_range[position] and not find_ans:
                    left_pos.append(position-attack_range[position])
                    stack_left.pop()
                    find_ans = True
                else:
                    stack_left.pop()
            if not find_ans:
                if len(stack_left) == 0:
                    left_pos.append(0)
                    stack_left.append(position)
                else:
                    left_pos.append(stack_left[-1] + 1)
                    stack_left.append(position)
            elif find_ans:
                stack_left.append(position)


    for position in range(len(strength  )-2,-1,-1 ):
        if strength  [stack_right[-1]] > strength  [position] :
            stack_right.append(position)
            right_pos.append(position)
        elif strength  [stack_right[-1]] == strength  [position]:
            stack_right.pop()
            stack_right.append(position)
            right_pos.append(position)
        else:
            find_ans = False
            while len(stack_right) != 0 and strength  [stack_right[-1]] < strength  [position]:

                if (stack_right[-1] - position) >= attack_range[position] and not find_ans:
                    right_pos.append(attack_range[position]+position)
                    stack_right.pop()
                    find_ans = True
                else:
                    stack_right.pop()
            if not find_ans:
                if len(stack_right) == 0:
                    right_pos.append(len(strength  ) - 1)
                    stack_right.append(position)
                else:
                    right_pos.append(stack_right[-1] - 1)
                    stack_right.append(position)
            elif find_ans:
                stack_right.append(position)

    right_pos.reverse()

    return left_pos,stack_left,right_pos,stack_right
left_pos,stack_left,right_pos,stack_right= stack(strength  ,attack_range)
print(strength  ,"\n",attack_range)
print(left_pos)
print(right_pos)





