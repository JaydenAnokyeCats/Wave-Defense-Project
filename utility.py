import pygame
import os

# This code makes it easier to get images, as opposed to typing in the path the image is stored in to access it.

Base_IMG_Path = 'Data/Assets/' # Base directory path where all image assets for the project are stored


def load_image(path):
    img = pygame.image.load(Base_IMG_Path + path).convert() # .convert() allows the image to be 'blitted' (drawn) onto the screen more effectively
    img.set_colorkey((0,0,0))
    return img



def load_images(path):
    images = []
    for img_name in sorted(os.listdir(Base_IMG_Path + path)):
        images.append(load_image(path + '/' + img_name))
        # Name of desired path, slash to separate, name of the image
    return images

