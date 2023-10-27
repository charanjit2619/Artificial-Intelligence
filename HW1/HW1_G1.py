#UCS
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


def ucs(val, goal_state):
    if val == goal_state:
        return "Input already in goal state!"
    import heapq
    visited = []
    open = []
    open.append(val)
    p = [(0, val)]
    heapq.heapify(p)
    actions_at_index = [[] for d in range(len(val))]
    final_state = ""
    steps = 0
    cost = 0
    parent_record = {}
    cost_record = {}

    action_cost = {
        1: 1,
        2: 1,
        3: 1,
        4: 1
    }
    a = ['1', '1', '1', '1', '1', '1', '1', '1', '1']

    for i in range(len(a)):
        a[i] = '0'
        for action in [1, 2, 3, 4]:
            if list(result(a, action)) == a:
                pass
            else:
                actions_at_index[i].append(action)
        a[i] = '1'

    while len(p) != 0:
        c, node = heapq.heappop(p)
        open.remove(node)
        visited.append(node)
        steps = steps + 1
        print("Parent Node: ",node)
        if node == goal_state:
            final_state = node
            visited.append(node)
            break
        for i in actions_at_index[node.index('0')]:
            child_node = result(node,i)
            if child_node not in open and child_node not in visited:
                print("Step No.: ",steps,"\nAction: ",i, "\nCurrent node: ", child_node, "\n")
                parent_record[child_node] = node
                cost_record[child_node] = c + action_cost[i]
                heapq.heappush(p,(c+action_cost[i],child_node))
                open.append(child_node)

            elif child_node in open:
                if cost_record[child_node] > (c+action_cost[i]):
                    p[p.index((cost_record[child_node],child_node))] = (c+action_cost[i], child_node)
                    heapq.heapify(p)
                    cost_record[child_node] = c + action_cost[i]
                else:
                    pass

    z = final_state
    path = [z]
    while z != val:
        path.append(parent_record[z])
        z = parent_record[z]

    path.reverse()

    return f'Final State: {final_state}\nTotal no. of Steps: {steps}\nPath: {path}\nTotal Cost: {c}'


while True:
    val = input("Enter the nine digit position as current state: >> ")
    if len(val) == 9 and val.isdigit():
        break
    else:
        print("Input not acceptable!")
goal_state = '123804765'
print(ucs(val, goal_state))

