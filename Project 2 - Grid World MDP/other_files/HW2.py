#transition_model

def transition_model(state, action):
    column_initial, row_initial, direction_initial = state

    blocked_states = [(2,2), (2,3), (3,2)]
    blocked_moves = []
    for z, y in blocked_states:
        for i in [1, 2, 3, 4]:
            blocked_moves.append((z,y,i))

    if (column_initial, row_initial, direction_initial) in [(2, 5, 4), (3, 5, 3), (5, 3, 1), (5, 4, 2), (1, 3, 4), (3, 1, 1)]:
        if action in ["A1", "A2"]:
            return column_initial, row_initial, direction_initial

    rotating_actions = [1, 3, 2, 4, 1, 3, 2, 4]
    if action == "A3":
        direction = rotating_actions[rotating_actions.index(direction_initial)+1]
    elif action == "A4":
        direction = rotating_actions[rotating_actions.index(direction_initial)-1]
    else:
        direction = direction_initial

    steps = 1
    action_definition = {
        1: (column_initial, (row_initial+steps), direction),
        2: (column_initial, row_initial-steps, direction),
        3: ((column_initial-steps), row_initial, direction),
        4: (column_initial+steps, row_initial, direction)
    }

    if action == 'A1':
        steps = 1
    elif action == 'A2':
        (c, r, d) = action_definition[direction_initial]
        if (c, r) in blocked_states or (c, r) in [(4, 4), (5, 5), (5, 3), (2, 5), (3, 5)]:
            return column_initial, row_initial, direction_initial
        else:
            steps = 2
    else:
        steps = 0

    action_definition = {
        1: (column_initial, (row_initial+steps), direction),
        2: (column_initial, row_initial-steps, direction),
        3: ((column_initial-steps), row_initial, direction),
        4: (column_initial+steps, row_initial, direction)
    }

    resulting_state = action_definition[direction_initial]
    (column, row, direction) = resulting_state

    if (resulting_state in blocked_moves) or row > 5 or column > 5 or row < 1 or column < 1:
        return column_initial, row_initial, direction_initial
    else:
        return resulting_state


#value iteration
discount_factor = 0.7
states = []
noise = 0
action_cost = {
    "A1": -1.5,
    "A2": -2,
    "A3": -0.5,
    "A4": -0.5
}

for i in [1, 2, 3, 4, 5]:
    for t in [1, 2, 3, 4, 5]:
        for robot_direction in [1, 2, 3, 4]:
            states.append((i, t, robot_direction))

state_value = {}
new_state_value = {}
states_best_Actions = {}

for x in states:
    state_value[x] = 0

for c, r, cost in [(4, 4, -1000), (5, 5, 100), (2, 3, -100000), (2, 2, -100000), (3, 2, -100000)]:
    for d in [1, 2, 3, 4]:
        state_value[(c, r, d)] = cost


def q_value(state,action):
    actions = ["A1", "A2", "A3", "A4"]
    actions.remove(action)
    qval = (1-noise)*(action_cost[action] + discount_factor*state_value[transition_model(state, action)])+\
           (noise/3)*(action_cost[actions[0]] + discount_factor*state_value[transition_model(state, actions[0])])+\
           (noise/3)*(action_cost[actions[1]] + discount_factor*state_value[transition_model(state,actions[1])])+\
           (noise/3)*(action_cost[actions[2]] + discount_factor*state_value[transition_model(state,actions[2])])
    return qval


for i in range(100):
    for (a, b, c) in states:
        if (a, b) in [(4, 4), (5, 5), (3, 2), (2, 2), (2, 3)]:
            new_state_value[(a, b, c)] = state_value[(a, b, c)]
            states_best_Actions[(a, b, c)] = new_state_value[(a, b, c)]
        else:
            states_best_Actions[(a, b, c)] = max([(q_value((a, b, c), act), act) for act in ["A1", "A2", "A3", "A4"]])
            new_state_value[(a, b, c)] = max([q_value((a, b, c), act) for act in ["A1", "A2", "A3", "A4"]])
    if i < 10:
        print(states_best_Actions)
    i += 1
    state_value = new_state_value
print(states_best_Actions)

def policy(state):
    (c, r, d) = state
    while (c, r) not in [(4, 4), (5, 5)]:
        (v, ac) = states_best_Actions[(c, r, d)]
        print(state, ac)
        state = transition_model((c, r, d), ac)
        (c, r, d) = state

policy((1,1,4))



