import random

import pygame

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("zvuky/pistol.wav")

herniOkno = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Chicken shooter")

pozadi = pygame.image.load("grafika/pozadi/les.jpg")
pozadi = pygame.transform.scale(pozadi, (1920, 1080))

obrazekZamerovace = pygame.image.load("grafika/zamerovac/crosshair.png")
obrazekZamerovace = pygame.transform.scale(obrazekZamerovace, (64, 64))
pygame.mouse.set_visible(False)
obrazekZamerovace_rect = obrazekZamerovace.get_rect()

obrazekSlepice = pygame.image.load("grafika/slepice/slepice00.png")
slepiceX = 0
slepiceY = 0
slepiceKrok = 10

hodiny = pygame.time.Clock()

hraBezi = True
while hraBezi:

    for event in pygame.event.get():
        # Pokud hrac kliknul na krizek, tak se nastavi promenna "hraBezi" na False (Nepravda)
        if event.type == pygame.QUIT:
            hraBezi = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.play()

    herniOkno.blit(pozadi, (0, 0))  # Vykresleni pozadi

    obrazekZamerovace_rect.center = pygame.mouse.get_pos()  # Nastaveni pozice kurzoru
    herniOkno.blit(obrazekZamerovace, obrazekZamerovace_rect)  # Vykresleni kurozru

    if slepiceX > 1920:
        slepiceX = 0
        slepiceY = random.randint(0, 1080)
    slepiceX = slepiceX + slepiceKrok

    herniOkno.blit(obrazekSlepice, (slepiceX, slepiceY))

    pygame.display.update()
    hodiny.tick(30)

pygame.quit()