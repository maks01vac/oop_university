import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.mixer.music.load('fon_sound.цфм')
pygame.mixer.music.play()
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    pygame.quit()