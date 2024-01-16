from sdf_ui import *

SIZE = (500, 1250)

beige = (0.933, 0.875, 0.753, 1)
blue = (0.059, 0.333, 0.569, 1)
red = (0.859, 0.161, 0.051, 1)
yellow = (0.890, 0.694, 0.102, 1)

transparency = lambda color: (*color[:3], 0)

if __name__ == "__main__":
    with Context(SIZE) as ctx:
        bg = clear_color(ctx, beige)

        distance = ctx.percent_y(25)
        radius = distance/2

        x = ctx.percent_x(50)
        y2 = ctx.percent_y(50)

        y1 = y2 - distance
        y3 = y2 + distance

        c1 = (x, y1)
        c2 = (x, y2)
        c3 = (x, y3)

        d1 = disc(ctx, c1, radius).generate_mask()
        d2 = disc(ctx, c2, radius).generate_mask()
        d3 = disc(ctx, c3, radius).generate_mask()

        b_bg = clear_color(ctx, blue)
        y_circle = disc(ctx, (-50, ctx.percent_y(30),), 400).fill(yellow, transparency(yellow))
        r_circle = disc(ctx, (SIZE[0]+50, ctx.percent_y(70)), 400).fill(red, transparency(red))

        circles = b_bg.alpha_overlay(y_circle).alpha_overlay(r_circle)

        bg = bg.mask(circles, d1.invert())
        bg = bg.mask(circles, d2.invert())
        bg = bg.mask(circles, d3.invert())

        bg = bg.alpha_overlay(film_grain(ctx).to_lab().transparency(0.05))

        bg.save("ample.png")