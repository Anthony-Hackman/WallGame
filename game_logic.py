import pygame
import random
import time

# Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
WALL_GAP_SIZE = 150
PLAYER_SPEED = 7
WALL_SPEED = 10

def create_wall():
    gap_start = random.randint(100, SCREEN_WIDTH - 100 - WALL_GAP_SIZE)
    return pygame.Rect(gap_start, 0, WALL_GAP_SIZE, 20)

def run_pygame_loop():
    
    global WALL_SPEED
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Walls by Hack")

    player = pygame.Rect((SCREEN_WIDTH - PLAYER_WIDTH) // 2, SCREEN_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
    wall = create_wall()
    score = 0
    font = pygame.font.Font(None, 36)

    game_running = True
    clock = pygame.time.Clock()

#Countdown before start
    for countdown in range(3, 0, -1):
        screen.fill((0, 0, 0))
        countdown_text = font.render(f'Starting in {countdown}...', True, (255, 255, 255))
        text_rect = countdown_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(countdown_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)

    while game_running:
        screen.fill((0, 0, 0))  # Clear screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
# controls
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.left > 0:
            player.x -= PLAYER_SPEED
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.right < SCREEN_WIDTH:
            player.x += PLAYER_SPEED
#wall generation
        wall.y += WALL_SPEED
        if wall.bottom > SCREEN_HEIGHT:
            wall = create_wall()
            score += 1
            if score % 5 == 0:
                WALL_SPEED += 1
# Collisions
        if wall.bottom >= player.top and wall.top <= player.bottom:
            if not (player.left > wall.left and player.right < wall.right):
                game_running = False

        pygame.draw.rect(screen, (255, 255, 255), player)
        pygame.draw.rect(screen, (255, 0, 0), (0, wall.y, wall.x, wall.height))
        pygame.draw.rect(screen, (255, 0, 0), (wall.right, wall.y, SCREEN_WIDTH - wall.right, wall.height))

        score_text = font.render(f'Walls: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # Ending Screen
    screen.fill((0, 0, 0))
    end_text1 = font.render("Game Over!", True, (255, 255, 255))
    end_text2 = font.render(f"Final Wall Count: {score}", True, (255, 255, 255))

    text_rect1 = end_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
    text_rect2 = end_text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))

    screen.blit(end_text1, text_rect1)
    screen.blit(end_text2, text_rect2)
    pygame.display.flip()

    # Wait for a few seconds
    pygame.time.wait(5000)
    
if __name__ == "__main__":
    run_pygame_loop()
