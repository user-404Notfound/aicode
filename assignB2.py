def water_jug_dfs(cap_a, cap_b, target):

    stack = [(0, 0, [])]
    visited = set()

    while stack:

        a, b, path = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == target or b == target:
            return path + [(a, b, "Goal")]

        
        moves = [
            ((cap_a, b), "Fill Jug A"),
            ((a, cap_b), "Fill Jug B"),
            ((0, b), "Empty Jug A"),
            ((a, 0), "Empty Jug B"),

            # Pour A -> B
            ((a - min(a, cap_b - b),
              b + min(a, cap_b - b)), "Pour A -> B"),

           
            ((a + min(b, cap_a - a),
              b - min(b, cap_a - a)), "Pour B -> A")
        ]


        for state, operation in reversed(moves):
            if state not in visited:
                stack.append((state[0], state[1],
                              path + [(a, b, operation)]))

    return None



cap_a = int(input("Enter capacity of Jug A: "))
cap_b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))


solution = water_jug_dfs(cap_a, cap_b, target)

if solution:
    print("\nDFS Solution:")

    for i, (a, b, operation) in enumerate(solution):
        print(f"Step {i}: {operation} -> ({a}, {b})")
else:
    print("\nNo solution possible.")
