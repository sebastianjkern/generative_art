# %%

from sdf_ui import *

from random import random, choice, randrange

import logging

from functools import reduce
from itertools import combinations

SIZE = (1000, 1250)

# TODO: Weird rect behaviour. 
# The Size of the rect is actually the size 
# of a quarter of the original rect, or only a corner
RECT_SIZE = (SIZE[0] - 550, SIZE[1] - 675)

logger().setLevel(logging.CRITICAL)

# Color palette
beige = (0.933, 0.875, 0.753, 1.0)
light_blue = (0.494, 0.627, 0.737, 1.0)
orange = (0.961, 0.749, 0.365, 1.0)
light_orange = (0.961, 0.749, 0.365, 1.0)
dark_grey = (0.184, 0.184, 0.184, 1.0)

colors = [light_blue, beige, orange, light_orange, dark_grey]

# Functions
def center():
    return SIZE[0] / 2, SIZE[1]/2

rand_point = lambda: (random() * SIZE[0], random() * SIZE[1])
rand_radius = lambda: randrange(SIZE[0] * 0.1, SIZE[0]*0.25)
transparency = lambda color: (color, (*color[:3], 0))

color = lambda: choice(colors)

rand_disc = lambda _: disc(ctx, rand_point(), rand_radius())

mask = lambda x: x.generate_mask()
fill = lambda x: x.fill(*transparency(color()))

overlay = lambda a, b: a.alpha_overlay(b)
show = lambda x: x.show()

intersect = lambda a, b: a.multiply(b)
subtract = lambda a, b: a.multiply(b.invert())


# Entry point
if __name__ == "__main__":
    with Context(SIZE) as ctx:
        rr = rounded_rect(ctx, center(), RECT_SIZE, (0, 0, 0, 0))
        rr_mask = rr.generate_mask()

        bg = rr.fill(dark_grey, beige, 0)
        
        discs = list(map(rand_disc, range(5)))
        masks = list(map(mask, discs))
        filled = list(map(fill, discs))

        circles = reduce(overlay, filled)

        for pair in combinations(masks, r=2):
            i = intersect(*pair)
            intersection = clear_color(ctx, (1, 1, 0, 1))

            circles = circles.mask(intersection, i.invert())

        bg = bg.mask(bg.alpha_overlay(circles), rr_mask.invert())
        bg = bg.alpha_overlay(film_grain(ctx).to_lab().transparency(0.05))
        bg.save("image.png")
