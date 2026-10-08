
def print_state(pegs):
    print(f"S = {pegs[0]}, A = {pegs[1]}, D = {pegs[2]}")


def tower_of_hanoi(n, source, auxiliary, destination, pegs):
    if n == 0:
        return


    tower_of_hanoi(n - 1, source, destination, auxiliary, pegs)


    disk = pegs[source].pop()
    pegs[destination].append(disk)


    names = ["S", "A", "D"]
    print(f"Move disk {disk}: {names[source]} -> {names[destination]}")


    print_state(pegs)
    print()


    tower_of_hanoi(n - 1, auxiliary, source, destination, pegs)


n = 3


pegs = [
    [3, 2, 1],   # Source
    [],          # Auxiliary
    []           # Destination
]

print("Initial State:")
print_state(pegs)
print()

# Solve Tower of Hanoi
tower_of_hanoi(n, 0, 1, 2, pegs)

print("Goal State:")
print_state(pegs)
