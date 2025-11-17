"""
Player entity - Cyberpunk Racer character
"""
import pygame
from typing import Optional


class Player(pygame.sprite.Sprite):
    """Player character with movement, jumping, and collision."""

    def __init__(self, x: int, y: int, sprite: Optional[pygame.Surface] = None):
        """
        Initialize player.

        Args:
            x: Starting x position
            y: Starting y position
            sprite: Player sprite image (optional)
        """
        super().__init__()

        # Set sprite or fallback to placeholder
        if sprite:
            self.original_sprite = sprite.copy()
            self.image = self.original_sprite.copy()
        else:
            # Placeholder graphics - cyan rectangle
            self.original_sprite = pygame.Surface((64, 64))
            self.original_sprite.fill((0, 255, 255))  # Cyan
            self.image = self.original_sprite.copy()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Direction tracking for sprite flipping
        self.facing_right = True

        # Physics properties (adjusted for background platforms)
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 6  # Slightly faster movement
        self.jump_power = -17  # Higher jump to reach platforms
        self.gravity = 0.7  # Slightly lower gravity for better air control
        self.on_ground = False

        # Invincibility
        self.invincible = False
        self.invincible_timer = 0
        
        # Sound manager reference (set by GameCore)
        self.sound_manager: Optional[object] = None
        
        # Jump tracking to avoid repeated jumps
        self.jump_pressed = False

    def update(self, platforms):
        """
        Update player state.

        Args:
            platforms: List of platform sprites for collision detection
        """
        # Handle keyboard input
        keys = pygame.key.get_pressed()

        # Horizontal movement
        self.velocity_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity_x = -self.speed
            # Flip sprite to face left
            if self.facing_right:
                self.facing_right = False
                self._update_sprite()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity_x = self.speed
            # Flip sprite to face right
            if not self.facing_right:
                self.facing_right = True
                self._update_sprite()

        # Jumping
        jump_key = keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]
        
        if jump_key and self.on_ground and not self.jump_pressed:
            self.velocity_y = self.jump_power
            self.on_ground = False
            self.jump_pressed = True
            if self.sound_manager:
                self.sound_manager.play('jump')
            print("Player jumped!")
        
        # Reset jump tracking when key is released
        if not jump_key:
            self.jump_pressed = False

        # Apply gravity
        self.velocity_y += self.gravity

        # Cap falling speed
        if self.velocity_y > 20:
            self.velocity_y = 20

        # Move horizontally
        self.rect.x += int(self.velocity_x)

        # Constrain to screen horizontally
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1536:
            self.rect.right = 1536

        # Move vertically
        self.rect.y += int(self.velocity_y)

        # Check platform collisions
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Landing on top of platform
                if self.velocity_y > 0 and self.rect.bottom <= platform.rect.top + 20:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                # Hit from below
                elif self.velocity_y < 0 and self.rect.top >= platform.rect.bottom - 20:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

        # Update invincibility timer
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False
                self._update_sprite()  # Reset sprite appearance
                print("Invincibility ended")

    def _update_sprite(self):
        """Update the sprite image based on direction and state."""
        # Start with original sprite
        sprite = self.original_sprite.copy()
        
        # Flip if facing left
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)
        
        # Tint purple when invincible
        if self.invincible:
            # Create a purple tint overlay
            tint = pygame.Surface(sprite.get_size()).convert_alpha()
            tint.fill((255, 0, 255, 128))  # Semi-transparent magenta
            sprite.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        self.image = sprite

    def activate_powerup(self):
        """Activate invincibility power-up."""
        self.invincible = True
        self.invincible_timer = 180  # 3 seconds at 60 FPS
        self._update_sprite()  # Update sprite appearance
        print("Invincibility activated!")

    def reset_position(self, x: int, y: int):
        """Reset player to starting position."""
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
