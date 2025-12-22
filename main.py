from tkinter.constants import TRUE

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

Game = TRUE


def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while Game == True:
        log_state()
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
