from sdf_ui import *

from scratch import Vector

from random import random

from functools import reduce


SIZE = Vector((1000, 1250))

transparency = lambda color: (*color[:3], 0)

red = hex_col("d13926")
dark_blue = hex_col("06403f")
lighter_blue = hex_col("075558")
white = hex_col("deb883")
yellow = hex_col("f1cb0e")

if __name__ == '__main__':
    with Context(tuple(SIZE)) as ctx:
        bg = clear_color(ctx, red)

        sun = disc(ctx, (ctx.percent_x(50), ctx.percent_y(77)), ctx.percent_x(22)).fill(yellow, transparency(yellow))

        bg = bg.alpha_overlay(sun)

        sea_sdf = rounded_rect(ctx, (ctx.percent_x(50), ctx.percent_y(24.9)), (ctx.percent_x(55), ctx.percent_y(25)), (0, 0, 0, 0))
        sea = sea_sdf.fill(dark_blue, transparency(dark_blue))

        bg = bg.alpha_overlay(sea)

        num_stripes = 12
        distance = ctx.percent_y(48) / (num_stripes)

        gap = distance * 0.1

        half_height = (distance-gap)/2

        gen_fill = lambda col: lambda x: x.fill(col, transparency(col))
        overlay = lambda a, b: a.alpha_overlay(b)

        rr_side = lambda c: rounded_rect(ctx, c, (ctx.percent_x(15) * (1 + random()), half_height), (half_height, half_height, half_height, half_height))

        # left dark stripes
        y_s = range(int(distance/2), int(ctx.percent_y(48)), int(distance))

        left_center = map(lambda y: (0, y), y_s)

        stripes = map(rr_side, left_center)
        filled = map(gen_fill(lighter_blue), stripes)

        bg = bg.alpha_overlay(reduce(overlay, filled))

        # right dark stripes
        right_center = map(lambda y: (ctx.percent_x(100), y), y_s)

        stripes = map(rr_side, right_center)
        filled = map(gen_fill(lighter_blue), stripes)

        bg = bg.alpha_overlay(reduce(overlay, filled))

        # center stripes

        gen_x = lambda _: ctx.percent_x(50) * (1+0.1*(random()-0.5))
        x_s = map(gen_x, y_s)

        center = list(zip(x_s, y_s))

        rr_center = lambda c: rounded_rect(ctx, c, (ctx.percent_x(10) * (1 + random()), half_height), (half_height, half_height, half_height, half_height))

        stripes = map(rr_center, center)
        filled = map(gen_fill(white), stripes)

        bg = bg.alpha_overlay(reduce(overlay, filled))

        # film grain and show
        bg = bg.alpha_overlay(film_grain(ctx).to_lab().transparency(0.05))
        bg.save("dawn2.png")
