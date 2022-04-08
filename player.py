import pygame.event

class Player:
    def __init__(self, x, y, dir_x, dir_y, size, color):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.color = color
        self.speed = 4
        self.size = size

    def move(self):
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
