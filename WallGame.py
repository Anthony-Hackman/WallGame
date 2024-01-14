import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
WALL_GAP_SIZE = 150
PLAYER_SPEED = 7
WALL_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Setup Pygame Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wall Game")

# Font
font = pygame.font.Font(None, 36)

# Player Setup
def create_player():
    return pygame.Rect((SCREEN_WIDTH - PLAYER_WIDTH) // 2, SCREEN_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

player = create_player()

# Wall Setup
def create_wall():
    gap_start = random.randint(100, SCREEN_WIDTH - 100 - WALL_GAP_SIZE)
    return pygame.Rect(gap_start, 0, WALL_GAP_SIZE, 20)

wall = create_wall()

# Main Menu
def main_menu():
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_running = False

        screen.fill(BLACK)
        menu_text = font.render('Press SPACE to start', True, WHITE)
        screen.blit(menu_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
        pygame.display.update()

# Game Loop
def game_loop():
    global wall, player, WALL_SPEED
    game_running = True
    clock = pygame.time.Clock()
    score = 0

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
            player.x += PLAYER_SPEED
            
        # Wall Movement
        wall.y += WALL_SPEED
        if wall.top > SCREEN_HEIGHT:
            wall = create_wall()
            score += 1
            if score % 5 == 0:
                WALL_SPEED += 1

        # Collision Detection
        if player.colliderect(wall):
            game_running = False

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, RED, (0, wall.y, wall.x, wall.height))
        pygame.draw.rect(screen, RED, (wall.right, wall.y, SCREEN_WIDTH - wall.right, wall.height))

        # Display Score
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Main
if __name__ == "__main__":
    main_menu()
    game_loop()
