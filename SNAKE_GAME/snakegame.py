import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

#we will declare global constant defination
speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE # we will keep both food and size os snake same
SEPARATION = 10 # separation between two pixels
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700
FPS = 25 
KEY = {"UP":1, "DOWN":2, "LEFT":3, "RIGHT":4}

# we will initialize screen
screen = pygame.display.set_mood((SCREEN_HEIGHT,SCREEN_HEIGHT).pygame.HWSURFACE)
#we havw used hw surface which stands for hardware surface refers to using memory on the video card for storing 
#draws as opposed to main memory

#Resources

scpre_


