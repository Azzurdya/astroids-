import sys
from tkinter.constants import TRUE
from traceback import print_exception

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import LINE_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from score_display import Score_tracker
from shot import Shot

asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
score = 0


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
    score = Score_tracker(0, "arcadeclassic/ARCADECLASSIC.TTF")

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
            for s in shots:
                if i.collides_with(s) == True:
                    log_event("asteroid_shot")
                    score.update(i)
                    s.kill()
                    i.split()

        for object in drawable:
            object.draw(screen)
        fps.tick(60)
        screen.blit(score.text, (10, 10))
        pygame.display.flip()


if __name__ == "__main__":
    main()
