---
applyTo: "src/game/**/*.py"
---

# Strong requirements

- Keep it simple : no extra classes if not mandatory, no unit test, no docs.md (just comments), no cicd
- Maximize the Pygame library out of the box components to limit custom code when provided by pygame
- Generate classes for the main components : game_core, game_inputs_manager, graphics_manager, sound_manager

# Technical requirements

- Python==3.12
- Game Engine : Pygame.py==2.6.0
- Pydantic==2.27.0
- package management : uv==0.9.7

# Implementation preferences

- models managed with pydantic over unstructured dict objects for improved legibility
- simple stdio prints for logging

# Pygame Documentation Resources

## Official Documentation

- **Main Documentation**: https://www.pygame.org/docs/
- **Pygame 2.x Documentation**: https://www.pygame.org/docs/ref/
- **Module Index**: https://www.pygame.org/docs/ref/index.html

**Note**: This project uses Pygame 2.6.0. The documentation links above cover the pygame 2.x API, which is compatible with version 2.6.0.

## Key Pygame Modules to Reference

### Core Modules

- **pygame.display**: Window and screen management - https://www.pygame.org/docs/ref/display.html
- **pygame.event**: Event handling (keyboard, mouse, gamepad) - https://www.pygame.org/docs/ref/event.html
- **pygame.Surface**: Graphics and image manipulation - https://www.pygame.org/docs/ref/surface.html
- **pygame.Rect**: Rectangle collision and positioning - https://www.pygame.org/docs/ref/rect.html

### Graphics and Rendering

- **pygame.draw**: Drawing shapes - https://www.pygame.org/docs/ref/draw.html
- **pygame.image**: Loading and saving images - https://www.pygame.org/docs/ref/image.html
- **pygame.sprite**: Sprite management - https://www.pygame.org/docs/ref/sprite.html
- **pygame.transform**: Scaling, rotating, flipping images - https://www.pygame.org/docs/ref/transform.html

### Input Management

- **pygame.key**: Keyboard input - https://www.pygame.org/docs/ref/key.html
- **pygame.mouse**: Mouse input - https://www.pygame.org/docs/ref/mouse.html
- **pygame.joystick**: Gamepad/joystick input - https://www.pygame.org/docs/ref/joystick.html

### Audio

- **pygame.mixer**: Sound and music playback - https://www.pygame.org/docs/ref/mixer.html
- **pygame.mixer.music**: Streaming music - https://www.pygame.org/docs/ref/music.html

### Utilities

- **pygame.time**: Time management and FPS control - https://www.pygame.org/docs/ref/time.html
- **pygame.font**: Text rendering - https://www.pygame.org/docs/ref/font.html
- **pygame.Color**: Color manipulation - https://www.pygame.org/docs/ref/color.html

## Usage Guidelines for 1 Hour Game Jam

### Maximize Built-in Components

- **Use pygame.sprite.Sprite and pygame.sprite.Group** for game entities instead of custom classes
- **Use pygame.Rect** for collision detection (colliderect, collidepoint, etc.)
- **Use pygame.time.Clock** for frame rate control
- **Use pygame.Surface.blit()** for drawing instead of complex rendering systems

## Examples and Tutorials

- **Pygame Examples Repository**: https://github.com/pygame/pygame/tree/main/examples
- **Game Tags on pygame.org**: https://www.pygame.org/tags/
- **Platformer Examples**: https://www.pygame.org/tags/platformer

## Best Practices for Quick Development

1. Start with pygame.sprite.Sprite for all game entities
2. Use pygame.sprite.Group for managing collections
3. Leverage pygame.Rect methods for collision and positioning
4. Use pygame.Surface.convert() or convert_alpha() after loading images for performance
5. Keep game state simple - use basic variables and lists
6. Use pygame.time.Clock.tick() to maintain consistent frame rate
7. Check pygame documentation when stuck - most features are already implemented

## When to Check Documentation

- Need to handle a specific input type → Check pygame.event, pygame.key, pygame.mouse, pygame.joystick
- Need to draw something → Check pygame.draw or pygame.Surface
- Need collision detection → Check pygame.Rect and pygame.sprite.collide functions
- Need to manage timing → Check pygame.time
- Need to load/manipulate images → Check pygame.image and pygame.transform
- Need sound effects → Check pygame.mixer
