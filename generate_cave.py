import random

GRID_SIZE = 50
INITIAL_CHANCE = .4
NUMBER_OF_STEPS = 3

# a dead cell surrounded by BIRTH_LIMIT or more cells becomes alive
# a live cell surrounded by less than DEATH_LIMIT cells dies
BIRTH_LIMIT = 4
DEATH_LIMIT = 3


def create_grid():
	choices = (1, 0)
	weights = (INITIAL_CHANCE, 1 - INITIAL_CHANCE)
	grid = [random.choices(choices, weights, k=GRID_SIZE) for i in range(GRID_SIZE)]
	return grid


def get_neighbors(grid, row, col):
	neighbors = 0

	# top
	if row > 0 and grid[row-1][col] == 1:
		neighbors += 1
	# bottom
	if row < GRID_SIZE - 1 and grid[row+1][col] == 1:
		neighbors += 1
	# left
	if col > 0 and grid[row][col-1] == 1:
		neighbors += 1
	# right
	if col < GRID_SIZE - 1 and grid[row][col+1] == 1:
		neighbors += 1
	# top left
	if row > 0 and col > 0 and grid[row-1][col-1] == 1:
		neighbors += 1
	# top right
	if row > 0 and col < GRID_SIZE - 1 and grid[row-1][col+1] == 1:
		neighbors += 1
	# bottom left
	if row < GRID_SIZE - 1 and col > 0 and grid[row+1][col-1] == 1:
		neighbors += 1
	# bottom right
	if row < GRID_SIZE -1 and col < GRID_SIZE - 1 and grid[row+1][col+1] == 1:
		neighbors += 1
	
	return neighbors


def update_cells(grid):
	for i in range(NUMBER_OF_STEPS):
		cells_to_live = []
		cells_to_kill = []

		for row in range(GRID_SIZE):
			for col in range(GRID_SIZE):
				cell = grid[row][col]
				neighbors = get_neighbors(grid, row, col)

				if cell == 1 and neighbors < DEATH_LIMIT:
					cells_to_kill.append((row, col))
				if cell == 0 and neighbors >= BIRTH_LIMIT:
					cells_to_live.append((row, col))

		for (r, c) in cells_to_live:
			grid[r][c] = 1
		for (r, c) in cells_to_kill:
			grid[r][c] = 0

	return grid


def generate_cave():
	grid = create_grid()
	grid = update_cells(grid)

	return grid
