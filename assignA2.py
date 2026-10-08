import heapq

# Input grid size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input start and goal
start = tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))

# Input obstacles
n = int(input("Enter number of obstacles: "))

obstacles = set()

for i in range(n):
    obstacle = tuple(map(int, input(f"Enter obstacle {i + 1} (row col): ").split()))
    obstacles.add(obstacle)


# A* heuristic: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Possible movements
moves = [
    (-1, 0, "Up"),
    (1, 0, "Down"),
    (0, -1, "Left"),
    (0, 1, "Right")
]


def get_neighbors(position):

    r, c = position
    neighbors = []

    for dr, dc, direction in moves:

        nr = r + dr
        nc = c + dc

        # Check boundary and obstacle
        if (0 <= nr < rows and
            0 <= nc < cols and
            (nr, nc) not in obstacles):

            neighbors.append(((nr, nc), direction))

    return neighbors


def a_star(start, goal):

    # Priority queue
    open_list = []

    heapq.heappush(open_list, (0, start))

    came_from = {}
    move_from = {}

    g_cost = {start: 0}

    visited = set()

    while open_list:

        f, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:

            path = []

            while current != start:
                path.append((current, move_from[current]))
                current = came_from[current]

            path.append((start, "Start"))
            path.reverse()

            return path, visited

        # Check possible moves
        for neighbor, direction in get_neighbors(current):

            new_cost = g_cost[current] + 1

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost

                f_cost = new_cost + heuristic(neighbor, goal)

                heapq.heappush(open_list, (f_cost, neighbor))

                came_from[neighbor] = current
                move_from[neighbor] = direction

    return None, visited


# Run A*
path, visited = a_star(start, goal)


# Display result
print("\n-----------------------------")
print("MODEL-BASED AGENT")
print("-----------------------------")

if path:

    print("\nAgent Navigation:")

    for i, (position, direction) in enumerate(path):

        print(f"Step {i + 1}: Agent at {position}")

        if direction != "Start":
            print("Move:", direction)

    print("\nGoal Reached Successfully!")
    print("Path:")

    for position, direction in path:
        print(position, end=" -> ")

    print("Goal")

else:
    print("\nNo path found!")
