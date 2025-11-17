"""
Cyberpunk Racer - Main Entry Point
A futuristic platformer game with cyberpunk aesthetics.
"""
import sys

import pygame

from game_core import GameCore


def main():
    """Initialize and run the game."""
    # Initialize Pygame
    pygame.init()

    # Create game window
    screen = pygame.display.set_mode((1536, 1024))
    pygame.display.set_caption("Cyberpunk Racer")

    # Create game clock for FPS control
    clock = pygame.time.Clock()

    # Create game core instance
    game = GameCore(screen)

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Update game state
        game.update()

        # Clear screen with black background
        screen.fill((0, 0, 0))

        # Draw game
        game.draw()

        # Update display
        pygame.display.flip()

        # Maintain 60 FPS
        clock.tick(60)

    # Cleanup
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
