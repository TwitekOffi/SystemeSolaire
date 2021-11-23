import pygame
import random
from pygame.math import Vector2


class Planete:
    def __init__(self):
        self.vitesse = Vector2(0, 0)

        # self.couleur = (255, 255, 0)
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.rayon = random.randint(5, 20)
        self.position = Vector2(random.randint(0, 500), random.randint(0, 500))
        self.direction = Vector2(0, 0)
        self.masse = random.randint(5, 14)
        self.Gravite = 10
        self.Fg = 0
        self.Fx = 0
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.l0 = 10
        self.L = 0

    def mouvement(self, MasseSoleil, positionSoleil):
        self.position = self.direction + self.position

        self.Ux = positionSoleil - self.position
        self.l = self.Ux.length()
        self.Ux = self.Ux.normalize()
        self.L = abs(self.l - self.l0)
        self.Fx = 0.0004 * self.L * self.Ux

        self.Fg = self.Gravite * ((MasseSoleil * self.masse) / self.l)
        #self.Fg = self.Fg * Vector2(1, 1)
        self.direction = self.direction + self.Fx

        self.position = self.direction + self.position


    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)


