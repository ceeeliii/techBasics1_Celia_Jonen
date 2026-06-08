import pygame
import random

# setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (135, 206, 235)  # sky blue
FPS = 60

# flower class
class Flower:
    def __init__(self):
        # random starting position
        self.x = random.randint(-100, -20)
        self.y = random.randint(100, SCREEN_HEIGHT - 150)

        # random speed
        self.speed = random.uniform(1.0, 3.5)

        # random size
        self.scale = random.uniform(0.6, 1.2)

        # random petal color
        self.petal_color = random.choice([
            (255, 182, 193),  # light pink
            (255, 105, 180),  # hot pink
            (216, 191, 216),  # thistle purple
            (255, 160, 122),])  # light salmon

    def draw(self, screen):
        cx = int(self.x)
        cy = int(self.y)
        s = self.scale

        # pot
        pot_rect = pygame.Rect(cx - int(35 * s), cy + int(80 * s), int(70 * s), int(50 * s))
        pygame.draw.rect(screen, (139, 69, 19), pot_rect)

        # stem
        stem_start = (cx, cy + int(80 * s))
        stem_end = (cx, cy - int(20 * s))
        pygame.draw.line(screen, (0, 128, 0), stem_start, stem_end, int(8 * s))

        # left leaf
        left_leaf_points = [
            (cx, cy + int(40 * s)),
            (cx - int(40 * s), cy + int(10 * s)),
            (cx - int(10 * s), cy + int(50 * s)),]
        pygame.draw.polygon(screen, (0, 100, 0), left_leaf_points)

        # right leaf
        right_leaf_points = [
            (cx, cy + int(55 * s)),
            (cx + int(40 * s), cy + int(25 * s)),
            (cx + int(10 * s), cy + int(65 * s)),]

        pygame.draw.polygon(screen, (0, 100, 0), right_leaf_points)

        # petals
        petal_radius = int(18 * s)
        petal_distance = int(28 * s)
        for i in range(8):
            angle_deg = i * 45
            angle_rad = pygame.math.Vector2(1, 0).rotate(-angle_deg)
            petal_x = cx + int(angle_rad.x * petal_distance)
            petal_y = cy + int(angle_rad.y * petal_distance)
            pygame.draw.circle(screen, self.petal_color, (petal_x, petal_y), petal_radius)

        # flower center
        pygame.draw.circle(screen, (255, 165, 0), (cx, cy), int(22 * s))

        # small yellow detail
        pygame.draw.circle(screen, (255, 255, 0), (cx, cy), int(10 * s))

    def update(self):
        # move flower to the right
        self.x += self.speed

        # reset when it goes off screen
        if self.x > SCREEN_WIDTH + 100:
            self.x = random.randint(-150, -20)
            self.y = random.randint(100, SCREEN_HEIGHT - 150)
            self.speed = random.uniform(1.0, 3.5)
            self.scale = random.uniform(0.6, 1.2)


# main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Floating Flower 🌸")
    clock = pygame.time.Clock()

    # create one single flower instance
    my_flower = Flower()

    # game loop
    running = True
    while running:

        # check if user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw background
        screen.fill(BACKGROUND_COLOR)

        # update and draw the flower
        my_flower.update()
        my_flower.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
