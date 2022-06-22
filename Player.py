import pygame
import Constants


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((35, 35))
        self.image.fill(Constants.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.centerx > Constants.WIDTH:
            self.rect.centerx = 0
        if self.rect.centery > Constants.HEIGHT:
            self.rect.centery = 0
        dX, dY = pygame.mouse.get_pos()[0] - self.rect.x, pygame.mouse.get_pos()[1] - self.rect.y
        try:
            self.speedx = (Constants.V ** 2) / (1 + abs(dY / dX)) * (dX / abs(dX))
        except ZeroDivisionError:
            self.speedx = 0
        try:
            self.speedy = (Constants.V ** 2) / (1 + abs(dX / dY)) * (dY / abs(dY))
        except ZeroDivisionError:
            self.speedy = 0