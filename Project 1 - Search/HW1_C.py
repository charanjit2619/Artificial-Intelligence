import random

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


while True:
    val = input("Enter the nine digit position as current state: >> ")
    if len(set(val)) == 9 and val.isdigit():
        break
    else:
        print("Input not acceptable!")


seq_action_state = []
actions = [1, 2, 3, 4]

while True:
    action = random.choice(actions)
    if val.isdigit():
        user_input_list = [int(d) for d in val]
        row_remainders = []
        dict = {
            3: 0,
            2: 0,
            1: 0
        }
        for i in dict.keys():
            for m in range(3):
                dict[i] = user_input_list.pop() + dict[i]

        for i in dict.keys():
            row_remainders.append((dict[i] % 3))
        if row_remainders == [0, 0, 0]:
            break
        else:
            val = result(val, action)

    else:
        val = result(val,action)

    seq_action_state.append((f'Action: {action},Achieved State: {val}'))

print(f'Final state: {val}')
print("The matrix is in goal state!")

if seq_action_state == []:
    print("No action taken!")
else:
    print(seq_action_state)