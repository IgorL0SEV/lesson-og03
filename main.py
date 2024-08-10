import pygame
import random


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("image/icon2.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("image/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 5
target_speed_y = 5
click_counter = 0
purpose_target = 3
font = pygame.font.Font(None, 36)

color = (random.randint(0, 200), random.randint(0, 200), random.randint(1,200))
color_font = (255, 255, 255)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        target_x += target_speed_x
        target_y += target_speed_y
        if target_x + target_width > SCREEN_WIDTH or target_x < 0:
            target_speed_x = -target_speed_x
        if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
            target_speed_y = -target_speed_y
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x+target_width and target_y < mouse_y < target_y+target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                click_counter +=1
    screen.blit(target_image, (target_x, target_y))
    text = font.render(f'Попадаений: {click_counter}/{purpose_target}', True, color_font)
    screen.blit(text, (10, 10))
    if click_counter == purpose_target:
        winner_text = font.render(f'Вы выиграили, количество попаданий: {purpose_target} !', True, color_font)
        screen.blit(winner_text, (10, 100))
        winner_text = font.render(f'Нажмите любую клавишу для выхода из программы.', True, color_font)
        screen.blit(winner_text, (10, 150))
    pygame.display.update()
    pygame.time.Clock().tick(60)
    if click_counter == purpose_target:
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
        running = False

pygame.quit()