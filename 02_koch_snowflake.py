import sys
import turtle

def koch_curve(t: turtle.Turtle, order: int, size: int):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(t: turtle.Turtle, order: int, size: int):
    t.right(-60)
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def main():
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    level = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    koch_snowflake(t, order=level, size=400)
    window.mainloop()


if __name__ == "__main__":
    main()
