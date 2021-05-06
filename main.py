import pygame
import sys
from button import Button

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sound Effects!")

like_image = pygame.image.load("like_button.png")
dislike_image = pygame.image.load("dislike_button.png")

like_hovering = pygame.image.load("like_hovering.png")
dislike_hovering = pygame.image.load("dislike_hovering.png")

like_button = Button(like_image, 200, 400)
dislike_button = Button(dislike_image, 600, 400)

like_sfx = pygame.mixer.Sound("like.mp3")
dislike_sfx = pygame.mixer.Sound("dislike.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if like_button.checkForInput(pygame.mouse.get_pos()):
                like_sfx.play()
            if dislike_button.checkForInput(pygame.mouse.get_pos()):
                dislike_sfx.play()
    
    screen.fill("white")
    
    like_button.update(screen)
    dislike_button.update(screen)
    
    if like_button.checkForInput(pygame.mouse.get_pos()):
        like_button.image = like_hovering
    else:
        like_button.image = like_image
    if dislike_button.checkForInput(pygame.mouse.get_pos()):
        dislike_button.image = dislike_hovering
    else:
        dislike_button.image = dislike_image
    
    pygame.display.update()