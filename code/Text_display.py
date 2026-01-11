import os

import pygame
from asteroid import *


class Static_Text(pygame.sprite.Sprite):
    def __init__(self, input, font_size, font_path):
        self.score = input
        self.font = pygame.font.Font(font_path, font_size)
        self.text = self.font.render(input, False, "white")


class Score_tracker(pygame.sprite.Sprite):
    def __init__(self, score, font_path) -> None:
        self.score = score
        self.font = pygame.font.Font(font_path, 40)
        self.text = self.font.render(f"score {self.score}", False, "white")

    def update(self, Astroid):
        self.score += (Astroid.radius // 30) + 1
        self.text = self.font.render(f"score {self.score}", False, "white")
