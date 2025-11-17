"""
Platform entities for level design
"""
import pygame


class Platform(pygame.sprite.Sprite):
    """Static platform that player can land on."""

    def __init__(self, x: int, y: int, width: int, height: int = 20):
        """
        Initialize platform.

        Args:
            x: X position
            y: Y position
            width: Platform width
            height: Platform height (default 20)
        """
        super().__init__()

        # Visible platform with semi-transparent overlay
        self.image = pygame.Surface((width, height))
        self.image.set_alpha(128)  # Semi-transparent
        self.image.fill((0, 255, 255))  # Cyan color for visibility
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def create_level_platforms():
    """
    Create a set of platforms matching the background level.png image.
    Platforms are positioned to align precisely with visible platforms in the background.
    Image size: 1536x1024

    Returns:
        pygame.sprite.Group: Group containing all platforms
    """
    platforms = pygame.sprite.Group()

    # Ground/bottom platform (extends across most of the bottom)
    platforms.add(Platform(0, 645, 615, 20))     # Left section of ground
    platforms.add(Platform(960, 645, 576, 20))   # Right section of ground

    # Lower left platform (above ground)
    platforms.add(Platform(0, 445, 370, 20))

    # Lower center platform (with cyan teleporter box)
    platforms.add(Platform(535, 535, 365, 20))

    # Upper left platform
    platforms.add(Platform(0, 298, 370, 20))

    # Upper center-right long platform (main high walkway)
    platforms.add(Platform(520, 293, 630, 20))

    return platforms
