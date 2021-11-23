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
        self.direction = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.masse = 10
        self.Gravite = 10
        self.Fg = Vector2()
        self.MaxFg = 1
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.MaxVitesse = 10

    def mouvement(self, MasseSoleil, positionSoleil):
        self.position = self.direction + self.position

        if self.vitesse.length() > self.MaxVitesse:
            self.vitesse = self.vitesse.normalize()
            self.vitesse = self.MaxVitesse * self.vitesse

        if self.Fg.length() > self.MaxFg:
            self.Fg = self.Fg.normalize()
            self.Fg = self.MaxFg * self.Fg

        self.Ux = positionSoleil - self.position
        self.l = self.Ux.length()
        self.Ux = self.Ux.normalize()

        self.Fg = self.Ux * self.Gravite * ((MasseSoleil * self.masse) / (self.l * self.l))

        self.direction = self.direction + self.Fg

        self.position = self.direction + self.position

    def draw(self, screen, posSoleil):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
        pygame.draw.line(screen ,(255,255,255), self.position, posSoleil,3 )
