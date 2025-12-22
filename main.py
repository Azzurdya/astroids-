import sys
from tkinter.constants import TRUE
from traceback import print_exception

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import LINE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot

asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    Game = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    fps = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    player_ship = Player(x, y, 10)
    astroid_feld = AsteroidField()

    while Game == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fps.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for i in asteroids:
            if i.collides_with(player_ship) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)
        pygame.draw.circle(screen, "white", (0, 0), 10, LINE_WIDTH)
        fps.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
