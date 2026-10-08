import heapq


def heuristic(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))

    return neighbors


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])


def a_star(start, goal):

    open_list = []

    g = 0
    h = heuristic(start, goal)
    f = g + h

    heapq.heappush(open_list, (f, g, start))

    closed = set()

    parent = {start: None}
    move_from_parent = {start: None}

    while open_list:

        f, g, current = heapq.heappop(open_list)

        if current in closed:
            continue

        closed.add(current)

        if current == goal:

            path = []
            moves = []

            while current is not None:
                path.append(current)
                moves.append(move_from_parent[current])
                current = parent[current]

            path.reverse()
            moves.reverse()

            print("\n========== SOLUTION ==========\n")

            for step, state in enumerate(path):

                g_value = step
                h_value = heuristic(state, goal)
                f_value = g_value + h_value

                print("Step:", step)

                if step > 0:
                    print("Move:", moves[step])

                print_puzzle(state)

                print("g(n) =", g_value)
                print("h(n) =", h_value)
                print("f(n) =", f_value)

                print("------------------------")

            print("Total moves:", len(path) - 1)

            return

        for neighbor, move in get_neighbors(current):

            if neighbor in closed:
                continue

            new_g = g + 1
            new_h = heuristic(neighbor, goal)
            new_f = new_g + new_h

            heapq.heappush(
                open_list,
                (new_f, new_g, neighbor)
            )

            if neighbor not in parent:
                parent[neighbor] = current
                move_from_parent[neighbor] = move

    print("No solution found.")


print("Enter Initial State")
print("Enter 9 numbers separated by spaces (0 = blank):")

start = tuple(map(int, input().split()))

print("\nEnter Goal State")
print("Enter 9 numbers separated by spaces (0 = blank):")

goal = tuple(map(int, input().split()))

print("\n========== INITIAL STATE ==========")

print_puzzle(start)

print("\ng(n) =", 0)
print("h(n) =", heuristic(start, goal))
print("f(n) =", heuristic(start, goal))

a_star(start, goal)
