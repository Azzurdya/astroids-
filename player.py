import constants
from circleshape import *
from shot import Shot


class Player(CircleShape):
    def __init__(
        self,
        x,
        y,
        radius,
    ):
        super().__init__(x, y, 10)
        self.rotation = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def draw(self, screen):
        shape = self.triangle()
        pygame.draw.polygon(screen, "white", shape, constants.LINE_WIDTH)

    def shoot(self):
        shot = Shot(self.position, constants.SHOT_RADIUS)
        shot_vector = pygame.Vector2(0, 1)
        rotated_shot_vector = shot_vector.rotate(self.rotation)
        shot.velocity = rotated_shot_vector * constants.PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
