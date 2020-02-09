from random import sample

paths = []
walls = []
player = []
guardian = []

with open('grid') as grid:
    for n, x in enumerate(grid):
        for m, y in enumerate(x):
            if y == "S":
                player.append((n, m))
            elif y == "G":
                guardian.append((n, m))
            elif y == ".":
                paths.append((n, m))
            else:
                walls.append((n, m))

xy_items = sample(paths, k=3)


print(player)
print("\n\n\n")
print(guardian)
print("\n\n\n")
print(paths)
print("\n\n\n")
print(walls)
print("\n\n\n")
print(xy_items)
