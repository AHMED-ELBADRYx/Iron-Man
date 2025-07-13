import turtle

# Define the three mask parts as lists of coordinates
piece1 = [
    [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40),
     (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],
    [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40),
     (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
]

piece2 = [
    [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30),
     (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],
    [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40),
     (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
]

piece3 = [
    [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280),
     (-60, -260), (-30, -260), (-20, -250), (0, -250)],
    [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),
     (110, -220), (80, -240), (60, -220), (0, -220)]
]

# Screen setup
turtle.hideturtle()
turtle.bgcolor('#ba161e')  # Dark maroon/red background
turtle.setup(500, 600)
turtle.title("I AM IRONMAN")
turtle.speed(2)

# Starting positions for each part
goto1 = (0, 120)
goto2 = (0, -30)
goto3 = (0, -220)

# Function to draw a piece using color fill
def draw_piece(piece, start):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.color('#fab104')  # Bright yellow/gold color
    turtle.begin_fill()
    for x, y in piece[0]:
        turtle.goto(x, y)
    for x, y in piece[1]:
        turtle.goto(x, y)
    turtle.end_fill()

# Call drawing for each part
try:
    draw_piece(piece1, goto1)
    draw_piece(piece2, goto2)
    draw_piece(piece3, goto3)
    turtle.hideturtle()
    turtle.done()
except turtle.Terminator:
    print("Drawing window was closed before finishing.")