"""
Enemy entities - Spider robots, humanoid robots, and flying vessels
"""
import math
import pygame
from typing import Optional


class SpiderRobot(pygame.sprite.Sprite):
    """Spider robot that patrols platforms horizontally."""

    def __init__(self, x: int, y: int, patrol_range: int = 150, sprite: Optional[pygame.Surface] = None):
        """
        Initialize spider robot.

        Args:
            x: Starting x position
            y: Starting y position
            patrol_range: Distance to patrol left/right
            sprite: Spider sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.original_sprite = sprite.copy()
            self.image = self.original_sprite.copy()
        else:
            # Placeholder graphics - red rectangle
            self.original_sprite = pygame.Surface((48, 48))
            self.original_sprite.fill((255, 0, 0))  # Red
            self.image = self.original_sprite.copy()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Patrol behavior
        self.start_x = x
        self.patrol_range = patrol_range
        self.speed = 2
        self.direction = 1  # 1 = right, -1 = left

    def update(self):
        """Update spider robot position."""
        self.rect.x += self.speed * self.direction

        # Reverse direction at patrol limits
        if self.rect.x > self.start_x + self.patrol_range:
            self.direction = -1
            self.image = pygame.transform.flip(self.original_sprite, True, False)
        elif self.rect.x < self.start_x - self.patrol_range:
            self.direction = 1
            self.image = self.original_sprite.copy()


class HumanoidRobot(pygame.sprite.Sprite):
    """Humanoid robot guard - static or slow patrol."""

    def __init__(self, x: int, y: int, patrol: bool = False, sprite: Optional[pygame.Surface] = None):
        """
        Initialize humanoid robot.

        Args:
            x: X position
            y: Y position
            patrol: Whether to patrol or stay static
            sprite: Humanoid sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.original_sprite = sprite.copy()
            self.image = self.original_sprite.copy()
        else:
            # Placeholder graphics - orange rectangle (taller)
            self.original_sprite = pygame.Surface((64, 80))
            self.original_sprite.fill((255, 165, 0))  # Orange
            self.image = self.original_sprite.copy()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Movement
        self.patrol = patrol
        self.speed = 1
        self.direction = 1
        self.start_x = x
        self.patrol_range = 100

    def update(self):
        """Update humanoid robot position."""
        if self.patrol:
            self.rect.x += self.speed * self.direction

            # Reverse at patrol limits and flip sprite
            if self.rect.x > self.start_x + self.patrol_range:
                self.direction = -1
                self.image = pygame.transform.flip(self.original_sprite, True, False)
            elif self.rect.x < self.start_x - self.patrol_range:
                self.direction = 1
                self.image = self.original_sprite.copy()


class FlyingVessel(pygame.sprite.Sprite):
    """Flying vessel that moves in wave pattern."""

    def __init__(self, x: int, y: int, sprite: Optional[pygame.Surface] = None):
        """
        Initialize flying vessel.

        Args:
            x: Starting x position
            y: Center y position for wave pattern
            sprite: Flying vessel sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.image = sprite.copy()
        else:
            # Placeholder graphics - yellow rectangle
            self.image = pygame.Surface((56, 40))
            self.image.fill((255, 255, 0))  # Yellow
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Wave movement
        self.center_y = y
        self.angle = 0
        self.speed = 1.5
        self.amplitude = 50  # Height of wave

    def update(self):
        """Update flying vessel with wave pattern."""
        self.rect.x -= int(self.speed)
        self.angle += 0.1
        self.rect.y = int(
            self.center_y + math.sin(self.angle) * self.amplitude)

        # Respawn on right side when off left side
        if self.rect.right < 0:
            self.rect.x = 1536


def create_level_enemies(graphics_manager=None):
    """
    Create enemies for the level, positioned on background platforms.

    Args:
        graphics_manager: Optional GraphicsManager for loading sprites

    Returns:
        pygame.sprite.Group: Group containing all enemies
    """
    enemies = pygame.sprite.Group()

    # Get sprites if graphics manager provided
    spider_sprite = graphics_manager.get_sprite('spider_robot') if graphics_manager else None
    humanoid_sprite = graphics_manager.get_sprite('humanoid_robot') if graphics_manager else None
    flying_sprite = graphics_manager.get_sprite('flying_vessel') if graphics_manager else None

    # Spider robots on platforms
    enemies.add(SpiderRobot(100, 397, 150, spider_sprite))      # Lower left platform (y=445-48=397)
    enemies.add(SpiderRobot(600, 487, 180, spider_sprite))      # Center platform (y=535-48=487)

    # Humanoid robots on high platforms
    enemies.add(SpiderRobot(150, 250, 120, humanoid_sprite))    # Upper left (y=298-48=250)
    enemies.add(HumanoidRobot(700, 213, patrol=True, sprite=humanoid_sprite))  # Upper center (y=293-80=213)

    # Flying vessels in air
    enemies.add(FlyingVessel(800, 400, flying_sprite))
    enemies.add(FlyingVessel(1200, 200, flying_sprite))

    return enemies
