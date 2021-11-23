import pygame
import random
from pygame.math import Vector2


class Soleil:
    def __init__(self):
        self.vitesse = Vector2(0, 0)
        self.Fg = 0
        self.couleur = (255, 255, 0)
        self.rayon = 15
        self.position = Vector2(250, 250)
        self.direction = Vector2(0, 0)
        self.masse = 10
        self.Gravite = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

