n = int(input("Enter number of cities: "))

cities = []

for i in range(n):
    cities.append(input(f"Enter city {i + 1}: ").upper())

dist = {}

print("\nEnter distances between cities (-1 for no connection):")

for city1 in cities:
    dist[city1] = {}

    for city2 in cities:
        if city1 == city2:
            dist[city1][city2] = 0
        elif city2 in dist and city1 in dist[city2]:
            dist[city1][city2] = dist[city2][city1]
        else:
            dist[city1][city2] = int(
                input(f"Distance {city1} -> {city2}: ")
            )

k = int(input("\nEnter beam width (k): "))
start = input("Enter starting city: ").upper()


def cost(path):
    total = 0

    for i in range(len(path) - 1):
        d = dist[path[i]][path[i + 1]]

        if d == -1:
            return float('inf')

        total += d

    return total


beam = []

for city in cities:
    if city != start and dist[start][city] != -1:
        beam.append([start, city])

beam.sort(key=cost)
beam = beam[:k]

print("\nInitial Beam:")

for path in beam:
    print(path, "Cost =", cost(path))


while beam and len(beam[0]) < len(cities):

    candidates = []

    for path in beam:

        for city in cities:

            if city not in path and dist[path[-1]][city] != -1:
                new_path = path + [city]
                candidates.append(new_path)

    candidates.sort(key=cost)
    beam = candidates[:k]

    print("\nCurrent Beam:")

    for path in beam:
        print(path, "Cost =", cost(path))


final_tours = []

for path in beam:

    if dist[path[-1]][start] != -1:

        tour = path + [start]

        total_cost = cost(path) + dist[path[-1]][start]

        final_tours.append((tour, total_cost))


if final_tours:

    best_tour, best_cost = min(
        final_tours,
        key=lambda x: x[1]
    )

    print("\nBest Tour:")
    print(" -> ".join(best_tour))
    print("Total Distance =", best_cost)

else:
    print("\nNo complete tour possible.")
