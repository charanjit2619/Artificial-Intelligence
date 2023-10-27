#DFS
def result(val,action):
    user_input = [int(a) for a in val]
    rows = [1,2,3]
    columns = [1,2,3]

    grid_index = []
    for row in rows:
        for column in columns:
            grid_index.append((row,column))

    dict1 = {
        1: (-1, 0),
        2: (1, 0),

        3: (0, -1),
        4: (0, 1)
    }

    (row_0, column_0) = grid_index[user_input.index(0)]
    (r, c) = dict1[action]
    new_row_0 = row_0+r
    new_column_0 = column_0+c

    if new_row_0 < 1 or new_column_0 < 1 or new_row_0 > 3 or new_column_0 > 3:
        pass #"Action Invalid! No change in the grid!"
    else:
        user_input[grid_index.index((row_0,column_0))] = user_input[grid_index.index((new_row_0,new_column_0))]
        user_input[grid_index.index((new_row_0, new_column_0))] = 0

    resulting_state = ""
    for i in user_input:
        resulting_state = resulting_state + f'{i}'

    return resulting_state


def dfs(val,goal_state):
    if val == goal_state:
        return "Input already in goal state!"
    visited = []
    stack = []
    stack.append(val)
    actions_at_index = [[] for d in range(len(val))]
    final_state = ""
    steps = 0
    parent_record = {}

    a = ['1', '1', '1', '1', '1', '1', '1', '1', '1']

    for i in range(len(a)):
        a[i] = '0'
        for action in [4,2,3,1]:
            if list(result(a, action)) == a:
                pass
            else:
                actions_at_index[i].append(action)
        a[i] = '1'

    while stack != []:
        node = stack.pop()
        visited.append(node)
        print("Parent Node: ",node)
        for i in actions_at_index[node.index('0')]:
            child_node = result(node,i)
            if child_node not in stack and child_node not in visited:
                parent_record[child_node] = node
                steps = steps + 1
                print("Step No.: ",steps,"\nAction: ",i, "\nResulting child node: ",child_node,"\n")
                if child_node == goal_state:
                    final_state = child_node
                    stack.clear()
                    break
                else:
                    stack.append(child_node)

    z = final_state
    path = [z]
    while z != val:
        path.append(parent_record[z])
        z = parent_record[z]

    path.reverse()

    return f'\nPath: {path}\nFinal State: {final_state}, Total no. of Steps: {steps}'


'''
To take input of game from user use the following code:
while True:
    val = input("Enter the nine digit position as current state: >> ")
    if len(set(val)) == 9 and val.isdigit():
        break
    else:
        print("Input not acceptable!")
'''

val = '724506831'
goal_state = '012345678'

print(dfs(val, goal_state))

#No. of steps: 111768
#No. of states in final path:  59627
