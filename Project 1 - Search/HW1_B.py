#Transition Model
def result(val,action):
    user_input = [int(a) for a in str(val)]
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

    row_0,column_0 = grid_index[user_input.index(0)]
    r,c = dict1[action]
    new_row_0 = row_0+r
    new_column_0 = column_0+c

    if new_row_0 < 1 or new_column_0 < 1 or new_row_0 > 3 or new_column_0 > 3:
        pass #Action Invalid! No change in the grid!
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

while True:
    action = input("Type an action:\n[1 for Up]\n[2 for Down]\n[3 for Left]\n[4 for Right] >> ")
    try:
        action = int(action)
        if action not in [1, 2, 3, 4]:
            print("Input not acceptable!")
        else:
            break
    except:
        print("Input not acceptable!")

print(result(val,action))