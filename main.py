import pygame
import os
pygame.font.init()
pygame.mixer.init()

# WINDOW
WIDTH, HEIGHT = 480, 320
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Game")

# FARBEN
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
NOT_PRESSED = (200, 200, 200)
PRESSED = (190, 190, 190)

# EINSTELLUNGEN
FPS = 60
SPD = FPS / 10


def draw_window(lanes):
    SCREEN.fill(BLACK)

    for lane in lanes:
        pygame.draw.rect(SCREEN, lane.c, pygame.Rect(
            lane.x, lane.y, lane.w, lane.h))

    pygame.display.update()


def main():
    class Lane:
        def __init__(self, x, y, w, h, c, p):
            self.x = x  # X-Koordinate
            self.y = y  # Y-Koordinate
            self.w = w  # Breite (width)
            self.h = h  # Hoehe (height)
            self.c = c  # Farbe (color)
            self.p = p  # Gedrueckt (pressed)

    lane1 = Lane(0, 0, WIDTH//4, HEIGHT, WHITE, False)
    lane2 = Lane(WIDTH//4, 0, WIDTH//4*2, HEIGHT, GRAY, False)
    lane3 = Lane(WIDTH//4*2, 0, WIDTH//4*3, HEIGHT, WHITE, False)
    lane4 = Lane(WIDTH//4*3, 0, WIDTH//4*4, HEIGHT, GRAY, False)
    lanes = [lane1, lane2, lane3, lane4]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    lane1.p = True
                if event.key == pygame.K_f:
                    lane2.p = True
                if event.key == pygame.K_j:
                    lane3.p = True
                if event.key == pygame.K_k:
                    lane4.p = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    lane1.p = False
                if event.key == pygame.K_f:
                    lane2.p = False
                if event.key == pygame.K_j:
                    lane3.p = False
                if event.key == pygame.K_k:
                    lane4.p = False
        for lane in lanes:
            if lane.p:
                lane.c = PRESSED
            else:
                lane.c = NOT_PRESSED

        draw_window(lanes)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
