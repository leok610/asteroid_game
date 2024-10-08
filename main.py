import pygame
from constants import *
from circleshape import *
from player import *

def main():
    # Initializes all submodules of pygame
    pygame.init()
    print("Starting asteroids!")

    # Display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Delta time variable
    dt = 0

    # Spawn player
    player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2)
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
