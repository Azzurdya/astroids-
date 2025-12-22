from tkinter.constants import TRUE

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


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
    Player.containers = (updatable, drawable)
    player_ship = Player(x, y, 10)

    while Game == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fps.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        fps.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
