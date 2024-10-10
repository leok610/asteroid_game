import pygame
from asteroidfield import *
from circleshape import *
from constants import *
from player import *
from shot import *

def main():
    # Initializes all submodules of pygame
    pygame.init()
    print("Starting asteroids!")

    # Display screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Delta time variable
    dt = 0

    # create object groups
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    # Add player classe to object groups and spawn player
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2)

    # Create asteroid object group and add asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add the AsteroidField object to updatable group
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    # Add the shot class to shots group
    Shot.containers = (shots, drawable, updatable)
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
