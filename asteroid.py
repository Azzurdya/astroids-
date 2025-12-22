import random

import constants
from circleshape import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, constants.LINE_WIDTH
        )

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity_vector = self.velocity
        print(velocity_vector)
        rotated_vector = velocity_vector.rotate(angle)
        rotated_vector2 = velocity_vector.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid1.velocity = rotated_vector * 1.2
        astroid2.velocity = rotated_vector2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
