"""
Sound Manager for Cyberpunk Racer
Handles loading and playing sound effects and music
"""
import pygame
from pathlib import Path
from typing import Dict, Optional


class SoundManager:
    """Manages all game audio including sound effects and music."""
    
    def __init__(self):
        """Initialize the sound manager and load all sound effects."""
        # Initialize pygame mixer if not already initialized
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        self.sounds: Dict[str, Optional[pygame.mixer.Sound]] = {}
        self.enabled = True
        self.volume = 0.5  # Default volume (0.0 to 1.0)
        
        # Load all sound effects
        self.load_sounds()
    
    def load_sound(self, name: str, path: str) -> bool:
        """
        Load a single sound effect.
        
        Args:
            name: Identifier for the sound
            path: Path to the sound file
            
        Returns:
            True if loaded successfully, False otherwise
        """
        try:
            sound_path = Path(path)
            if sound_path.exists():
                sound = pygame.mixer.Sound(str(sound_path))
                sound.set_volume(self.volume)
                self.sounds[name] = sound
                print(f"Loaded sound: {name} from {path}")
                return True
            else:
                print(f"Sound file not found: {path}")
                self.sounds[name] = None
                return False
        except Exception as e:
            print(f"Error loading sound {name}: {e}")
            self.sounds[name] = None
            return False
    
    def load_sounds(self):
        """Load all game sound effects."""
        # Base path for assets (relative to game directory)
        base_path = Path(__file__).parent.parent.parent / "assets" / "sounds"
        
        # Load each sound effect
        self.load_sound('jump', str(base_path / 'jump.wav'))
        self.load_sound('collect', str(base_path / 'collect.wav'))
        self.load_sound('hit', str(base_path / 'hit.wav'))
        self.load_sound('win', str(base_path / 'win.wav'))
        
        print(f"SoundManager initialized. Loaded {sum(1 for s in self.sounds.values() if s is not None)}/{len(self.sounds)} sounds.")
    
    def play(self, name: str):
        """
        Play a sound effect by name.
        
        Args:
            name: The identifier of the sound to play
        """
        if not self.enabled:
            return
        
        sound = self.sounds.get(name)
        if sound:
            sound.play()
        else:
            print(f"Sound not found or not loaded: {name}")
    
    def set_volume(self, volume: float):
        """
        Set the volume for all sound effects.
        
        Args:
            volume: Volume level (0.0 to 1.0)
        """
        self.volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            if sound:
                sound.set_volume(self.volume)
    
    def toggle_enabled(self):
        """Toggle sound effects on/off."""
        self.enabled = not self.enabled
        return self.enabled
    
    def stop_all(self):
        """Stop all currently playing sounds."""
        pygame.mixer.stop()
