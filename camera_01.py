import sys
import time
from unicodedata import name
import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()


def get_frame():
    image = cam.get_image()
    frame = pygame.image.tostring(image, 'RGB')
    return frame

if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))

    while 1:
            image = cam.get_image()
            data = pygame.image.tostring(image,"RGB")
            img = pygame.image.fromstring(data,(640,480),"RGB")
            screen.blit(img,(0,0))
            pygame.display.update()
