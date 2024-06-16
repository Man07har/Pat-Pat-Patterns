import pygame
import sys
import time

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 36)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rabin-Karp Algorithm Simulation")

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    # Calculate hash of the pattern
    pattern_hash = sum(ord(pattern[i]) for i in range(m))

    for i in range(n - m + 1):
        # Calculate hash of the current substring of text
        text_hash = sum(ord(text[i + j]) for j in range(m))
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            matches.append(i)

    return matches

def draw_text(text, x, y, color=WHITE):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    pattern_hash = sum(ord(pattern[i]) for i in range(len(pattern)))

    running = True
    i = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        current_text = text[i:i + len(pattern)]
        current_hash = sum(ord(current_text[j]) for j in range(len(current_text)))

        draw_text(f"Text: {text}", 20, 20)
        draw_text(f"Pattern: {pattern}", 20, 60)
        draw_text(f"Checking text from position {i} to {i + len(pattern)}: {current_text}", 20, 100)
        draw_text(f"Text Hash: {current_hash}", 20, 140)

        if current_hash == pattern_hash and current_text == pattern:
            draw_text("Pattern found!", 20, 180, RED)

        pygame.display.flip()
        time.sleep(1)  # Sleep for 1 second to simulate the animation
        i += 1

        if i > len(text) - len(pattern):
            i = 0

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
