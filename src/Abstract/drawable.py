import pygame
from PIL import Image

class Drawable:
    def __init__(self, image_file):
        image = Image.open(image_file, 'r')
        image_width, image_height = image.size
        self._rect = pygame.Rect(0,0, image_width, image_height)
        self._sprite = [[]]