import os

import pygame
from asteroid import *


class Static_Text(pygame.sprite.Sprite):
    def __init__(self, text, font_size, font_path):
        self.score = text
        self.font = pygame.font.Font(font_path, font_size)


class Score_tracker(Static_Text):
    def __init__(self, text, font_size, font_path):
        super().__init__(text, font_size, font_path)
        self.text = self.font.render(f"score {self.score}", False, "white")

    def update(self, Astroid):
        self.score += (Astroid.radius // 30) + 1
        self.text = self.font.render(f"score {self.score}", False, "white")


class Titles(Static_Text):
    def __init__(self, text, font_size, font_path):
        super().__init__(text, font_size, font_path)
        self.text = self.font.render(text, False, "white")

    def update(self, text):
        self.text = self.font.render(text, False, "white")
