from circleshape import *
from constants import *
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = uniform(20, 50)
        # Rotating returns a vector object with the x y coordinates after rotation
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn1 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn2 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn1.velocity = new_velocity1 * 1.2
        spawn2.velocity = new_velocity2 * 1.2

