from generate_cave import *
from PIL import Image, ImageDraw

WHITE = (255, 255, 255)
cave = generate_cave()

# create a new image
size_ratio = 30
img_size = GRID_SIZE * size_ratio 
cave_img = Image.new('RGB', size=(img_size, img_size))


def generate_image():
	global cave_img
	draw = ImageDraw.Draw(cave_img)

	for row in range(GRID_SIZE):
		for col in range(GRID_SIZE):
			if cave[row][col] == 1:
				draw.rectangle((row * size_ratio, col * size_ratio,\
				 row * size_ratio + size_ratio, col * size_ratio + size_ratio), fill=WHITE)

	return cave_img


generate_image()
cave_img.show()
