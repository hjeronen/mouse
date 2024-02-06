import math

# map settings
height = 21
width = 21

# images
empty = 0
tile = 1
mouse = 2
cat = 3

# starting points
mouse_start_x = math.floor(width/2)
mouse_start_y = math.floor(height/2)
cat_one_start = (math.floor(width/2), 1)
cat_two_start = (math.floor(width/2), height - 2)
cat_three_start = (1, math.floor(height/2))
cat_four_start = (width - 2, math.floor(height/2))
