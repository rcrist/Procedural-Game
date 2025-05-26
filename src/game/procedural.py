import random


def generate_level():
    # Example of a simple level generation algorithm
    level = []
    for i in range(10):  # Generate 10 rows
        row = []
        for j in range(10):  # Generate 10 columns
            if random.random() < 0.2:  # 20% chance of a wall
                row.append(1)  # Wall
            else:
                row.append(0)  # Empty space
        level.append(row)
    return level

def generate_enemies(level):
    enemies = []
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 0 and random.random() < 0.1:  # 10% chance to spawn an enemy
                enemies.append((i, j))  # Enemy position
    return enemies

def generate_items(level):
    items = []
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 0 and random.random() < 0.05:  # 5% chance to spawn an item
                items.append((i, j))  # Item position
    return items