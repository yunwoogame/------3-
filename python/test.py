import pygame

pygame.init()

screen_width = 200
screen_height = 200

# 화면 너비와 높이를 튜플로 전달합니다.
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 유지를 위한 기본 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()