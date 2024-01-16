from sdf_ui import *

SIZE = (1000, 1500)

red = (0.875, 0.110, 0.133, 1)
grey = (0.133, 0.196, 0.192, 1)

transparency = lambda color: (*color[:3], 0)

if __name__ == "__main__":
    with Context(SIZE) as ctx:
        x = ctx.percent_x(50)
        y1 = ctx.percent_y(30)
        y2 = ctx.percent_y(70)

        c1 = (x, y1)
        c2 = (x, y2)

        circle1 = disc(ctx, c1, ctx.percent_x(25))
        circle2 = disc(ctx, c2, ctx.percent_x(25))

        # bigger circles
        bc1 = circle1.fill(red, transparency(red), inflate=20)
        bc2 = circle2.fill(grey, transparency(grey), inflate=20)

        # smaller circles
        sc1 = circle1.fill(grey, transparency(grey), inflate=-20)
        sc2 = circle2.fill(red, transparency(red), inflate=-20)

        # rects
        rr1 = rounded_rect(ctx, (0, ctx.percent_y(50)), (ctx.percent_x(50), ctx.percent_y(50)), (0, 0, 0, 0)).fill(red, transparency(red))

        # background
        bg = clear_color(ctx, grey)

        bg = bg.alpha_overlay(rr1)
        bg = bg.alpha_overlay(bc1)
        bg = bg.alpha_overlay(bc2)
        bg = bg.alpha_overlay(sc1)
        bg = bg.alpha_overlay(sc2)

        bg = bg.alpha_overlay(film_grain(ctx).to_lab().transparency(0.05))

        bg.save("black_and_red.png")
