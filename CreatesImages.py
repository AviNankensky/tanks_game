import pygame

# pygame.init()


def create_summary_image(kills, coins, level):


    width, height = 400, 300
    surface = pygame.Surface((width, height))
    surface.fill((255, 255, 255))  # רקע לבן

    # שימוש בגופן ברירת מחדל של Pygame
    font = pygame.font.Font(None, 30)

    text_color = (0, 0, 0)  # צבע שחור לטקסט

    texts = [
        f"סיכום שלב {level}",
        f"הריגות: {kills}",
        f"מטבעות: {coins}"
    ]

    for i, text in enumerate(texts):
        text_surface = font.render(text, True, text_color)
        surface.blit(text_surface, (20, 20 + i * 50))

    return surface


# דוגמה לשימוש
level = 1
kills = 10
coins = 50

# יצירת החלון של Pygame
screen = pygame.display.set_mode((400, 300))

# יצירת תמונת הסיכום
summary_surface = create_summary_image(kills, coins, level)

# הצגת התמונה במשחק
screen.blit(summary_surface, (0, 0))
pygame.display.flip()

# לולאת המשחק
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
