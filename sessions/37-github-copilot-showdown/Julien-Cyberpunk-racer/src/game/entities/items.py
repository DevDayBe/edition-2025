"""
Collectible items - Energy orbs, power-ups, and holographic gem
"""
import pygame
from typing import Optional


class EnergyOrb(pygame.sprite.Sprite):
    """Small collectible that gives points."""

    def __init__(self, x: int, y: int, sprite: Optional[pygame.Surface] = None):
        """
        Initialize energy orb.

        Args:
            x: X position
            y: Y position
            sprite: Energy orb sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.image = sprite.copy()
        else:
            # Placeholder graphics - green rectangle
            self.image = pygame.Surface((24, 24))
            self.image.fill((0, 255, 0))  # Green
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = 10


class PowerUp(pygame.sprite.Sprite):
    """Power-up that gives invincibility."""

    def __init__(self, x: int, y: int, sprite: Optional[pygame.Surface] = None):
        """
        Initialize power-up.

        Args:
            x: X position
            y: Y position
            sprite: Power-up sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.image = sprite.copy()
        else:
            # Placeholder graphics - purple rectangle
            self.image = pygame.Surface((32, 32))
            self.image.fill((160, 32, 240))  # Purple
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = 50


class HolographicGem(pygame.sprite.Sprite):
    """Win condition item - the goal of the game."""

    def __init__(self, x: int, y: int, sprite: Optional[pygame.Surface] = None):
        """
        Initialize holographic gem.

        Args:
            x: X position
            y: Y position
            sprite: Holographic gem sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.image = sprite.copy()
        else:
            # Placeholder graphics - white rectangle
            self.image = pygame.Surface((48, 48))
            self.image.fill((255, 255, 255))  # White
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.points = 500


def create_level_items(graphics_manager=None):
    """
    Create collectible items for the level, positioned on background platforms.

    Args:
        graphics_manager: Optional GraphicsManager for loading sprites

    Returns:
        tuple: (energy_orbs group, powerups group, gem sprite)
    """
    energy_orbs = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    # Get sprites if graphics manager provided
    orb_sprite = graphics_manager.get_sprite('energy_orb') if graphics_manager else None
    powerup_sprite = graphics_manager.get_sprite('power_up') if graphics_manager else None
    gem_sprite = graphics_manager.get_sprite('holographic_gem') if graphics_manager else None

    # Energy orbs on platforms (adjusted to corrected positions)
    # Ground platforms (y=645)
    energy_orbs.add(EnergyOrb(200, 615, orb_sprite))
    energy_orbs.add(EnergyOrb(400, 615, orb_sprite))
    energy_orbs.add(EnergyOrb(1050, 615, orb_sprite))
    energy_orbs.add(EnergyOrb(1250, 615, orb_sprite))
    
    # Lower left platform (y=445)
    energy_orbs.add(EnergyOrb(80, 415, orb_sprite))
    energy_orbs.add(EnergyOrb(180, 415, orb_sprite))
    energy_orbs.add(EnergyOrb(280, 415, orb_sprite))
    
    # Center platform with teleporter (y=535)
    energy_orbs.add(EnergyOrb(600, 505, orb_sprite))
    energy_orbs.add(EnergyOrb(700, 505, orb_sprite))
    energy_orbs.add(EnergyOrb(800, 505, orb_sprite))
    
    # Upper left platform (y=298)
    energy_orbs.add(EnergyOrb(100, 268, orb_sprite))
    energy_orbs.add(EnergyOrb(220, 268, orb_sprite))
    
    # Upper center platform (y=293)
    energy_orbs.add(EnergyOrb(650, 263, orb_sprite))
    energy_orbs.add(EnergyOrb(850, 263, orb_sprite))
    energy_orbs.add(EnergyOrb(1000, 263, orb_sprite))

    # Power-ups on strategic platforms
    powerups.add(PowerUp(350, 415, powerup_sprite))      # Lower left
    powerups.add(PowerUp(750, 505, powerup_sprite))      # Center platform
    powerups.add(PowerUp(950, 263, powerup_sprite))      # Upper center

    # Holographic gem at the end of the upper platform
    gem = HolographicGem(1080, 245, gem_sprite)

    return energy_orbs, powerups, gem
