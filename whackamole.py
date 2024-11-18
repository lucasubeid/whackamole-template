import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_y = (random.randrange(0, 16))
        mole_x = (random.randrange(0, 20))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = event.pos
                    row = x//32
                    col = y//32
                    if row == mole_x and col == mole_y:
                        mole_y = (random.randrange(0, 16))
                        mole_x = (random.randrange(0, 20))
                        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * 32, mole_y * 32)))

            screen.fill("dark green")
            for i in range(1,21):
                pygame.draw.line(screen, "black", (i*32,0),(i*32,512))
            for i in range(1,17):
                pygame.draw.line(screen, "black", (0, i*32), (640, i*32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x*32, mole_y*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
