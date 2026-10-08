from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    level = 0

    while queue:
        print("\n========== LEVEL", level, "==========")

        for _ in range(len(queue)):
            state, path = queue.popleft()

            print("\nState:")
            print(state[0], state[1], state[2])
            print(state[3], state[4], state[5])
            print(state[6], state[7], state[8])

            if state == goal:
                print("\nGoal Found!")
                return path

            zero = state.index(0)
            row = zero // 3
            col = zero % 3

            moves = [
                (-1, 0, "UP"),
                (1, 0, "DOWN"),
                (0, -1, "LEFT"),
                (0, 1, "RIGHT")
            ]

            for dr, dc, move in moves:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < 3 and 0 <= nc < 3:
                    new_zero = nr * 3 + nc

                    new_state = list(state)
                    new_state[zero], new_state[new_zero] = \
                        new_state[new_zero], new_state[zero]

                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [move]))

        level += 1

    return None


def get_grid_input(prompt):
    print(prompt)
    grid = []

    for _ in range(3):
        grid.extend(map(int, input().split()))

    return tuple(grid)


start = get_grid_input("Enter Initial State (3 rows, 0 for blank):")
goal = get_grid_input("Enter Goal State (3 rows):")

solution = bfs(start, goal)

if solution:
    print("\nSolution:")
    print(" -> ".join(solution))
    print("Total moves:", len(solution))
else:
    print("\nNo solution exists.")
