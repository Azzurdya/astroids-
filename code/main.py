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
from Text_display import *

asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print("all text from Jakob Fischer at www.pizzadude.dk")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    Game = True
    game_state = 1
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    fps = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    resetable = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable, resetable)
    Asteroid.containers = (asteroids, updatable, drawable, resetable)
    Player.containers = (updatable, drawable, resetable)
    Score_tracker.containers = resetable
    player_ship = Player(x, y, 10)
    astroid_feld = AsteroidField()
    score = Score_tracker(0, 40, "arcadeclassic/ARCADECLASSIC.TTF")
    title = Titles("ASTROIDS", 100, "arcadeclassic/ARCADECLASSIC.TTF")
    screen.fill("black")
    screen.blit(title.text, (400, 300))
    while Game == True:
        while game_state == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    for i in resetable:
                        i.kill()
                    score = Score_tracker(0, 40, "arcadeclassic/ARCADECLASSIC.TTF")
                    player_ship = Player(x, y, 10)
                    game_state = 2

            fps.tick(60)
            pygame.display.flip()

        while game_state == 2:
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            dt = fps.tick(60) / 1000
            screen.fill("black")
            updatable.update(dt)
            for i in asteroids:
                if i.collides_with(player_ship) == True:
                    title.update("GAME OVER!")
                    game_state = 3
                for s in shots:
                    if i.collides_with(s) == True:
                        log_event("asteroid_shot")
                        score.update(i)
                        s.kill()
                        i.split()

            for object in drawable:
                object.draw(screen)
            screen.blit(score.text, (10, 10))
            fps.tick(60)

            pygame.display.flip()

        while game_state == 3:
            screen.fill("black")
            screen.blit(title.text, (400, 300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    game_state = 1

            fps.tick(60)
            pygame.display.flip()


if __name__ == "__main__":
    main()
