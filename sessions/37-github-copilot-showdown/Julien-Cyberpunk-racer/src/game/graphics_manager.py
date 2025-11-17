"""
Graphics Manager for Cyberpunk Racer
Handles loading and managing all game sprites and backgrounds
"""
import pygame
from pathlib import Path
from typing import Dict, Optional, Tuple


class GraphicsManager:
    """Manages all game graphics including sprites and backgrounds."""
    
    def __init__(self):
        """Initialize the graphics manager and load all assets."""
        self.sprites: Dict[str, Optional[pygame.Surface]] = {}
        self.backgrounds: Dict[str, Optional[pygame.Surface]] = {}
        
        # Base paths for assets
        self.base_path = Path(__file__).parent / "assets"
        self.sprites_path = self.base_path / "sprites"
        self.backgrounds_path = self.base_path / "backgrounds"
        
        # Load all assets
        self.load_all_assets()
    
    def load_image(self, path: Path, convert_alpha: bool = True) -> Optional[pygame.Surface]:
        """
        Load an image file.
        
        Args:
            path: Path to the image file
            convert_alpha: Whether to convert with alpha transparency
            
        Returns:
            Loaded pygame Surface or None if failed
        """
        try:
            if path.exists():
                if convert_alpha:
                    image = pygame.image.load(str(path)).convert_alpha()
                else:
                    image = pygame.image.load(str(path)).convert()
                print(f"Loaded: {path.name}")
                return image
            else:
                print(f"File not found: {path}")
                return None
        except Exception as e:
            print(f"Error loading {path.name}: {e}")
            return None
    
    def load_sprite(self, name: str, filename: str, size: Optional[Tuple[int, int]] = None) -> Optional[pygame.Surface]:
        """
        Load a sprite with optional scaling.
        
        Args:
            name: Identifier for the sprite
            filename: Relative path from sprites directory
            size: Optional (width, height) to scale to
            
        Returns:
            Loaded sprite or None
        """
        path = self.sprites_path / filename
        image = self.load_image(path, convert_alpha=True)
        
        if image and size:
            image = pygame.transform.scale(image, size)
        
        self.sprites[name] = image
        return image
    
    def load_background(self, name: str, filename: str) -> Optional[pygame.Surface]:
        """
        Load a background image.
        
        Args:
            name: Identifier for the background
            filename: Filename in backgrounds directory
            
        Returns:
            Loaded background or None
        """
        path = self.backgrounds_path / filename
        image = self.load_image(path, convert_alpha=False)
        self.backgrounds[name] = image
        return image
    
    def load_all_assets(self):
        """Load all game assets."""
        print("\n=== Loading Graphics ===")
        
        # Load character sprites
        print("Loading characters...")
        self.load_sprite('player', 'characters/player.png', (64, 64))
        self.load_sprite('spider_robot', 'characters/spider_robot.png', (48, 48))
        self.load_sprite('humanoid_robot', 'characters/humanoid_robot.png', (64, 80))
        self.load_sprite('flying_vessel', 'characters/flying_vessel.png', (56, 40))
        self.load_sprite('boss', 'characters/boss_cyborg_baguette.png', (128, 160))  # Final boss - Cyborg Baguette
        
        # Load item sprites
        print("Loading items...")
        self.load_sprite('energy_orb', 'items/energy_orb.png', (24, 24))
        self.load_sprite('power_up', 'items/power_up.png', (32, 32))
        self.load_sprite('holographic_gem', 'items/holographic_gem.png', (48, 48))
        
        # Load backgrounds
        print("Loading backgrounds...")
        self.load_background('level', 'level.png')
        self.load_background('splashscreen', 'splashscreen.png')
        
        # Summary
        sprites_loaded = sum(1 for s in self.sprites.values() if s is not None)
        backgrounds_loaded = sum(1 for b in self.backgrounds.values() if b is not None)
        print(f"\nGraphics loaded: {sprites_loaded}/{len(self.sprites)} sprites, {backgrounds_loaded}/{len(self.backgrounds)} backgrounds")
        print("======================\n")
    
    def get_sprite(self, name: str) -> Optional[pygame.Surface]:
        """Get a loaded sprite by name."""
        return self.sprites.get(name)
    
    def get_background(self, name: str) -> Optional[pygame.Surface]:
        """Get a loaded background by name."""
        return self.backgrounds.get(name)
    
    def get_flipped_sprite(self, name: str, flip_x: bool = True, flip_y: bool = False) -> Optional[pygame.Surface]:
        """
        Get a flipped version of a sprite.
        
        Args:
            name: Sprite name
            flip_x: Flip horizontally
            flip_y: Flip vertically
            
        Returns:
            Flipped sprite or None
        """
        sprite = self.get_sprite(name)
        if sprite:
            return pygame.transform.flip(sprite, flip_x, flip_y)
        return None
