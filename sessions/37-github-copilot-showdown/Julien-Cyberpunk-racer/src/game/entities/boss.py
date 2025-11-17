"""
Boss entity - Final boss Cyborg Baguette
"""
import pygame
from typing import Optional


class Boss(pygame.sprite.Sprite):
    """Final boss - Cyborg Baguette with patrol movement."""

    def __init__(self, x: int, y: int, sprite: Optional[pygame.Surface] = None):
        """
        Initialize boss.

        Args:
            x: Starting x position
            y: Starting y position
            sprite: Boss sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.original_sprite = sprite.copy()
            self.image = self.original_sprite.copy()
        else:
            # Placeholder graphics - large red-orange rectangle
            self.original_sprite = pygame.Surface((128, 160))
            self.original_sprite.fill((255, 100, 50))  # Red-orange
            self.image = self.original_sprite.copy()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Boss health
        self.max_health = 5
        self.health = self.max_health
        self.invincible_timer = 0  # Temporary invincibility after being hit

        # Movement properties
        self.start_x = x
        self.patrol_range = 200  # Distance to patrol left/right
        self.speed = 1.5
        self.direction = 1  # 1 = right, -1 = left

    def update(self):
        """Update boss position and state."""
        # Update invincibility timer
        if self.invincible_timer > 0:
            self.invincible_timer -= 1

        # Patrol movement
        self.rect.x += int(self.speed * self.direction)

        # Reverse direction at patrol limits and flip sprite
        if self.rect.x > self.start_x + self.patrol_range:
            self.direction = -1
            self.image = pygame.transform.flip(self.original_sprite, True, False)
        elif self.rect.x < self.start_x - self.patrol_range:
            self.direction = 1
            self.image = self.original_sprite.copy()

    def take_damage(self):
        """
        Boss takes damage from player (when player is invincible).
        
        Returns:
            bool: True if boss was defeated, False otherwise
        """
        if self.invincible_timer > 0:
            return False
        
        self.health -= 1
        self.invincible_timer = 60  # 1 second invincibility after being hit
        
        # Flash effect (optional visual feedback)
        print(f"Boss hit! Health: {self.health}/{self.max_health}")
        
        return self.health <= 0

    def is_defeated(self) -> bool:
        """Check if boss is defeated."""
        return self.health <= 0


def create_boss(graphics_manager=None):
    """
    Create the final boss.

    Args:
        graphics_manager: Optional GraphicsManager for loading sprite

    Returns:
        Boss: The boss instance
    """
    # Get boss sprite if graphics manager provided
    boss_sprite = graphics_manager.get_sprite('boss') if graphics_manager else None
    
    # Place boss on the upper center platform (y=293)
    # Position at the end of the platform
    boss = Boss(1000, 133, boss_sprite)  # y = 293 - 160 (boss height) = 133
    
    return boss
