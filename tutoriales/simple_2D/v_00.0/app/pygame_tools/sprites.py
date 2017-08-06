# coding=utf-8

import pygame



def split_sprite(sheet, start, size, columns, resize):
    frames = []
    for i in range(columns):
        location = (start[0]+size[0]*i, start[1])
        img = sheet.subsurface(pygame.Rect(location, size))
        img = pygame.transform.scale(img, (resize[0], resize[1]) )
        frames.append(img)
    return frames





class human:
    def __init__(self, size):
        self.sprite = pygame.image.load('app/static/images/human_sprite.png')
        self.s_width = self.sprite.get_rect().size[0] / 8.0
        self.s_height = self.sprite.get_rect().size[1] /3.0
        print "Size: ", self.sprite.get_rect().size
        self.h = int(size)
        self.w = int( (size/self.s_height) * self.s_width )
        self.items = int(self.sprite.get_rect().size[0]/self.s_width)
        self.walking = split_sprite(self.sprite, (0, self.s_height), (self.s_width, self.s_height), self.items, (self.w, self.h))
        self.running = split_sprite(self.sprite, (0, 0), (self.s_width, self.s_height), self.items, (self.w, self.h))
        

    def walk(self, i):
        if i < self.items:
            return self.walking[i]
        else:
            return self.walking[0]

    def run(self, i):
        if i < self.items:
            return self.running[i]
        else:
            return self.running[0]
