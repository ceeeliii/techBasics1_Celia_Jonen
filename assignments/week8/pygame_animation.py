__import__('pygame')

#Flower (from week 3 I want to use here)
# setup
('from turtle import')

setup(600, 600)
bgcolor("skyblue")
tracer(0, 0)

# draw pot
penup()
goto(-35, -220)
pendown()
color("saddlebrown")
begin_fill()
for i in range(2):
    forward(120)
    left(90)
    forward(80)
    left(90)
end_fill()

# draw flower stem
penup()
goto(25, -140)
pendown()
color("green")
pensize(12)
setheading(90)
forward(180)

# left leaf
penup()
goto(20, -40)
pendown()
setheading(140)
color("darkgreen")
begin_fill()
circle(60, 70)
left(110)
circle(60, 70)
end_fill()

# right leaf
penup()
goto(40, -70)
pendown()
setheading(40)
begin_fill()
circle(50, 70)
left(100)
circle(60, 70)
end_fill()

# flower center
penup()
goto(0, 60)
pendown()
pensize(1)
color("orange")
begin_fill()
circle(30)
end_fill()

# petals
for angle in range(0, 360, 45):
    penup()
    goto(30, 65)
    setheading(angle)
    forward(50)
    pendown()
    color("pink")
    begin_fill()
    circle(25)
    end_fill()

# little details in the center
penup()
goto(25, 60)
pendown()
color("yellow")
begin_fill()
circle(8)
end_fill()

# finish
update()
exitonclick()


#Dino setup from class
# importing required library



# activate the pygame library
pygame.init()

# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
# use convert_alpha() for png images
img = pygame.image.load("flower.png").convert_alpha()

# scale down the flower
img = pygame.transform.scale(img, (100,100))

# option: tint your image if you want

img.fill(("pink"), special_flags=pygame.BLEND_ADD)

# position of dino
flower_x = 100
flower_y = 100

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # moving flower as clock tick
    if flower_x  < SCREEN_WIDTH:
        flower_y += 3
    else:
        flower_x = 0

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)
    # Using blit to copy image to screen at a specific location
    screen.blit(img, (flower_x, flower_y))
    # refresh the display
    pygame.display.flip()

pygame.quit()
exit(0)
