
def vacuum_agent(location, status):
    # Condition-Action Rules
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"



tiles = {
    "A": input("Enter status of Tile A (Dirty/Clean): ").capitalize(),
    "B": input("Enter status of Tile B (Dirty/Clean): ").capitalize()
}

location = input("Enter initial agent location (A/B): ").upper()


print("\nInitial State:")
print("Tile A:", tiles["A"])
print("Tile B:", tiles["B"])
print("Agent Location:", location)



for step in range(1, 5):

    status = tiles[location]

    # Get action from reflex agent
    action = vacuum_agent(location, status)

    print("\nStep", step)
    print("Percept:", [location, status])
    print("Action:", action)

    # Perform action
    if action == "Suck":
        tiles[location] = "Clean"

    elif action == "Right":
        location = "B"

    elif action == "Left":
        location = "A"

    print("Tile A:", tiles["A"])
    print("Tile B:", tiles["B"])
    print("Agent Location:", location)


print("\nFinal State:")
print("Tile A:", tiles["A"])
print("Tile B:", tiles["B"])
print("Agent Location:", location)
