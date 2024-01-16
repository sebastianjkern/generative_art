from sdf_ui import *

from random import random, choice

SIZE = (1000, 1250)

red = hex_col("cc411e")
yellow = hex_col("f4b82f")
blue = hex_col("1c328b")

colors = ["f1b82b", "268ac2", "499fae", "c32c1b", "ee8a2d", "f57b78", "2c8956", "eac1b0", "cc411e", "f4b82f"]

transparency = lambda color: (*color[:3], 0)

color = lambda: hex_col(choice(colors))

if __name__ == "__main__":
    with Context(SIZE) as ctx:
        bg = clear_color(ctx, red)

        sea_sdf = rounded_rect(ctx, (ctx.percent_x(50), ctx.percent_y(24.9)), (ctx.percent_x(55), ctx.percent_y(25)), (0, 0, 0, 0))
        sea = sea_sdf.fill(blue, transparency(blue))
        sea_mask = sea_sdf.generate_mask()

        transparent = clear_color(ctx, (0, 0, 0, 0))
        sun = disc(ctx, (ctx.percent_x(50), ctx.percent_y(50)), ctx.percent_x(25)).fill(yellow, transparency(yellow))

        sun = sun.mask(transparent, sea_mask.invert())

        bg = bg.alpha_overlay(sea).alpha_overlay(sun)

        num_stripes = 20

        size = (ctx.percent_x(25), 5)
        distance = (ctx.percent_y(50)-40) / 20

        stripes_y = range(20, int(ctx.percent_y(50))-20, int(distance))
        stripes_x = map(lambda _: ctx.percent_x(50) + (random()-0.5)*ctx.percent_x(25), stripes_y)

        centers = list(zip(stripes_x, stripes_y))

        for center in centers:
            col = color()
            rr = rounded_rect(ctx, center, size, (0, 0, 0, 0)).fill(col, transparency(col))

            bg = bg.alpha_overlay(rr)

        bg = bg.alpha_overlay(film_grain(ctx).to_lab().transparency(0.05))

        bg.save("dawn.png")
