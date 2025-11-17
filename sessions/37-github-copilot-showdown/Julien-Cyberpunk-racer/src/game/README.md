# Game Metadata

**Game Name**: Cyberpunk Racer

**Game Theme**: Futuristic / Cyberpunk

**Game Genre**: Platformer

**Game Pitch**: This is a futuristic platformer game where a cyberpunk racer will be facing spider robots, humanoid robots, flying vessels in it's quest for the holographic gem.

**Core Mechanics**:
- **Player Movement**: Left/Right running, Jump (with gravity), possible Double Jump for advanced platforming
- **Platform Navigation**: Jump between platforms, avoid falling into pits
- **Enemy Avoidance**: Dodge or jump over enemies (spider robots, humanoid robots, flying vessels)
- **Collectibles**: Gather coins/energy orbs for points, find the holographic gem to win
- **Hazards**: Falling off platforms = lose life, touching enemies = lose life
- **Win Condition**: Collect the holographic gem and reach the end zone
- **Lose Condition**: Run out of lives (start with 3 lives)

**Input Management**:
- **Keyboard Primary Controls**:
  - Arrow Keys: LEFT/RIGHT for movement, UP or SPACE for jump
  - Alternative: W/A/S/D (A/D for movement, W or SPACE for jump)
  - ESC: Pause/Menu
  - R: Restart game
- **Mouse (Optional)**:
  - Click on menu buttons (Start, Restart, Quit)

**Scoring Mechanisms**:
- **Points System**:
  - Collect energy orbs: +10 points each
  - Collect power-ups: +50 points each
  - Defeat/avoid enemies: +25 points per enemy passed
  - Collect holographic gem: +500 points (win condition)
- **Lives System**: Start with 3 lives, lose 1 life per:
  - Falling off platform
  - Collision with enemy
  - Game Over when lives = 0
- **Time Bonus (Optional)**: Faster completion = higher score multiplier

---

# Graphic Design Decisions

**Style**: Cyberpunk / Neon Futuristic with dark backgrounds and bright neon accents

**Color Palette**:
- Background: Dark blue/purple/black gradient (night sky or cyber city)
- Player: Bright cyan/electric blue with neon accents
- Enemies: Red, orange, yellow (danger colors with metallic texture)
- Collectibles: Green (energy orbs), Purple/Pink (power-ups), Glowing white/cyan (holographic gem)
- Platforms: Dark gray/black with neon edge lighting (cyan, pink, or purple)

**Sprites Point of View**: Side view (2D platformer perspective)

## Backgrounds

### Splashscreen Background (assets/backgrounds/splashscreen.png)
- **Type**: Menu/Title screen background
- **Style**: Digital painting with smooth gradients and atmospheric lighting
- **Resolution**: 1536x1024 (landscape)
- **Description**: Dramatic cyberpunk cityscape viewed from street level, featuring towering neon-lit skyscrapers, holographic advertisements, flying vehicles with light trails, and atmospheric rain effects. Dark backgrounds with bright cyan, pink, and purple neon accents create high contrast for menu text visibility.

### Level Background (assets/backgrounds/level.png)
- **Type**: Gameplay background for platformer level
- **Style**: Highly detailed pixel art with crisp edges
- **Resolution**: 1536x1024 (landscape)
- **Point of View**: Side view (2D platformer perspective) with clear horizontal layers
- **Description**: Multi-layered cyberpunk city environment designed for side-scrolling gameplay. Features distant silhouetted skyscrapers, mid-ground industrial structures with neon lighting, and foreground platform areas. Dark metallic platforms with cyan and purple neon underlighting. Minimal decorative elements to maintain focus on gameplay. Parallax-ready with distinct depth layers for smooth scrolling.

## Main Character Description

**Player Character**: Cyberpunk Racer
- Humanoid figure with sleek futuristic armor/suit
- Glowing cyan/electric blue accents on body (visor, chest piece, legs)
- Athletic build, dynamic running pose
- Helmet with illuminated visor
- Size: ~64x64 pixels for sprite

## Enemies Descriptions

### Enemy 1: Spider Robot
- Mechanical spider with 4-6 legs
- Red glowing eyes/core
- Metallic gray/black body with red accents
- Crawls on platforms horizontally
- Size: ~48x48 pixels
- Behavior: Patrols left-right on platforms

### Enemy 2: Humanoid Robot
- Tall bipedal robot guard
- Orange/yellow glowing chest core
- Angular, industrial design
- Stands in fixed positions or slow patrol
- Size: ~64x80 pixels (taller than player)
- Behavior: Static guard or slow horizontal movement

### Enemy 3: Flying Vessel
- Small drone or hovering ship
- Yellow/orange propulsion glow
- Sleek, angular design with wings/rotors
- Size: ~56x40 pixels
- Behavior: Flies in wave pattern or circles above platforms

## Sprite Descriptions

### Item 1: Energy Orb (Collectible)
- Small glowing sphere
- Green pulsing glow
- Size: ~24x24 pixels
- Purpose: +10 points, scattered throughout level

### Item 2: Power-Up Crystal
- Larger angular crystal shape
- Purple/pink glow with sparkle effect
- Size: ~32x32 pixels
- Purpose: +50 points, temporary invincibility (3 seconds)

### Item 3: Holographic Gem (Win Objective)
- Large multi-faceted gem
- Bright cyan/white glow with rainbow refraction
- Size: ~48x48 pixels
- Purpose: +500 points, triggers win condition
- Location: At the end of the level

## Obstacle Descriptions

### Obstacle 1: Platform Gaps
- Empty space between platforms
- Deadly fall (lose 1 life)
- Visual: Dark void or distant city lights far below

### Obstacle 2: Moving Platforms (Optional)
- Platforms that move horizontally or vertically
- Same visual style as static platforms but animated
- Challenge: Timing jumps correctly

### Obstacle 3: Laser Barriers (Optional)
- Vertical or horizontal red laser beams
- Instant death or damage on contact
- Animated flickering/pulsing

---

# Project Structure

```
src/game/
├── main.py                 # Entry point, game initialization
├── game_core.py           # Main game loop, state management
├── game_inputs_manager.py # Keyboard/mouse input handling
├── graphics_manager.py    # Sprite loading, rendering, animations
├── sound_manager.py       # Sound effects and music (Phase 4+)
├── entities/
│   ├── player.py         # Player sprite class
│   ├── enemies.py        # Enemy sprite classes
│   └── items.py          # Collectible/item sprite classes
├── requirements.txt       # Python dependencies (pygame, pydantic)
└── README.md             # This file (game documentation)

assets/
├── sprites/
│   ├── characters/
│   │   ├── player.png
│   │   ├── spider_robot.png
│   │   ├── humanoid_robot.png
│   │   └── flying_vessel.png
│   └── items/
│       ├── energy_orb.png
│       ├── power_up.png
│       └── holographic_gem.png
├── backgrounds/
│   ├── splashscreen.png    # Menu/title screen background
│   └── level.png           # Gameplay level background
└── sounds/ (Phase 4+)
    ├── jump.wav
    ├── collect.wav
    ├── hit.wav
    └── win.wav
```

---

# Current Phase Guidance

## **PHASE 1: CONCEPT & SETUP** (15 min) - ✅ COMPLETE

### Status: All Phase 1 deliverables completed successfully!

### Completed:
✅ Game theme defined: Futuristic Cyberpunk Platformer
✅ Core mechanics specified: Platformer with enemies, collectibles, lives system
✅ Input controls defined: Keyboard (Arrow keys / WASD + SPACE)
✅ Scoring mechanisms: Points for collectibles, lives system, win/lose conditions
✅ Characters & enemies: Cyberpunk racer, 3 enemy types (spider, humanoid, flying)
✅ Items: Energy orbs, power-ups, holographic gem (win objective)
✅ Visual style: Dark cyberpunk with neon accents, side-view 2D
✅ Project structure created (all files and directories in place)
✅ Dependencies installed (pygame 2.6.0, pydantic 2.12.4)
✅ Pygame initialized with 1536x1024 window
✅ Game loop running at 60 FPS with proper event handling
✅ GameState management with pydantic BaseModel
✅ Basic UI rendering (score, lives, state display)

---

## **PHASE 2: ASSET GENERATION** (20 min) - ✅ COMPLETE

### Status: All visual assets generated successfully!

### Completed:
✅ **Character Sprites** (saved in `/assets/sprites/characters/`):
   - Player sprite: Cyberpunk racer (64x64px, cyan/electric blue)
   - Spider robot enemy (48x48px, red glow, mechanical legs)
   - Humanoid robot enemy (64x80px, orange/yellow core)
   - Flying vessel enemy (56x40px, yellow propulsion)

✅ **Item Sprites** (saved in `/assets/sprites/items/`):
   - Energy orb (24x24px, green glow)
   - Power-up crystal (32x32px, purple/pink glow)
   - Holographic gem (48x48px, cyan/white rainbow refraction)

✅ **Background** (saved in `/assets/backgrounds/`):
   - Cyberpunk city scene (1536x1024px, dark with neon accents)

### Validation Results:
✅ All PNG files with transparency created
✅ Sprites match size specifications
✅ Cyberpunk aesthetic maintained
✅ Assets ready for integration

---

## **PHASE 3: CORE GAMEPLAY** (30 min) - ✅ COMPLETE

### Status: Fully playable game with placeholder graphics!

### Completed:
✅ **Player Entity** (`entities/player.py`):
   - Player class with pygame.sprite.Sprite
   - Cyan rectangle placeholder (64x64)
   - Horizontal movement (arrow keys / WASD)
   - Jump with gravity physics
   - Platform collision detection
   - Invincibility system for power-ups

✅ **Platform System** (`entities/platform.py`):
   - 11 platforms created at different heights
   - Dark gray rectangle placeholders
   - Collision detection working
   - Multi-level platforming layout

✅ **Enemy System** (`entities/enemies.py`):
   - SpiderRobot: Red 48x48, horizontal patrol
   - HumanoidRobot: Orange 64x80, static/slow patrol
   - FlyingVessel: Yellow 56x40, wave movement
   - 6 enemies spawned strategically

✅ **Item System** (`entities/items.py`):
   - EnergyOrb: Green 24x24, 13 orbs placed, +10 points
   - PowerUp: Purple 32x32, 3 placed, +50 points + invincibility
   - HolographicGem: White 48x48, 1 placed, +500 points + WIN

✅ **Game Logic** (`game_core.py`):
   - Full state management (MENU → PLAYING → GAME_OVER/WIN)
   - Lives system (start with 3)
   - Score tracking with all collectibles
   - Collision detection (platforms, enemies, items)
   - Death handling (fall off screen, enemy hit)
   - Respawn system with timer
   - Menu screen with instructions
   - Game Over screen with final score
   - Win screen with final score
   - Restart functionality (R key)

### Validation Results:
✅ Game loop runs at 60 FPS
✅ Player movement and jumping responsive
✅ Platform collisions working correctly
✅ Enemy movement patterns functional
✅ Item collection working with score/effects
✅ Lives decrease on damage
✅ Game Over triggers when lives = 0
✅ Win condition works (collect gem)
✅ Full game flow from start to end
✅ Test suite passes (test_gameplay.py)

---

## **PHASE 4: GRAPHICS INTEGRATION & POLISH** (25 min) - ✅ COMPLETE

**Goal**: Replace placeholder rectangles with actual sprites, add backgrounds, sounds, and polish

**Status**: All Phase 4 deliverables completed successfully! Game now features full sprite integration and audio system.

**Important**: This phase transformed the functional game into a visually appealing experience.

### Deliverables (Development Team):

#### 1. **Graphics Manager Setup** (`graphics_manager.py`) - ✅ COMPLETE:
   - ✅ Created GraphicsManager class
   - ✅ Implemented sprite loading with `pygame.image.load()`
   - ✅ Applied transparency with `.convert_alpha()`
   - ✅ Scaled sprites to match exact sizes (64x64, 48x48, etc.)
   - ✅ Cached loaded images for performance
   - ✅ Graceful handling of missing files (fallback to colored rectangles)
   - ✅ Load summary reporting (7/7 sprites, 2/2 backgrounds loaded)

#### 2. **Sprite Integration** (`entities/*.py`) - ✅ COMPLETE:
   - ✅ **Player** (`entities/player.py`):
     - Replaced cyan rectangle with player.png sprite (64x64)
     - Sprite flipping for left/right direction
     - Purple tint overlay for invincibility state
   
   - ✅ **Enemies** (`entities/enemies.py`):
     - Replaced colored rectangles with enemy sprites
     - SpiderRobot: spider_robot.png (48x48) with patrol flipping
     - HumanoidRobot: humanoid_robot.png (64x80) with patrol flipping
     - FlyingVessel: flying_vessel.png (56x40)
   
   - ✅ **Items** (`entities/items.py`):
     - Replaced colored rectangles with item sprites
     - EnergyOrb: energy_orb.png (24x24)
     - PowerUp: power_up.png (32x32)
     - HolographicGem: holographic_gem.png (48x48)

#### 3. **Background Integration** (`game_core.py`) - ✅ COMPLETE:
   - ✅ Loaded level.png background (1536x1024)
   - ✅ Background draws before all sprites
   - ✅ Fallback to dark color if background missing

#### 4. **Sound Effects** (`sound_manager.py`) - ✅ COMPLETE:
   - ✅ Created SoundManager class
   - ✅ Sound loading using `pygame.mixer.Sound()`
   - ✅ Sounds integrated on events:
     - Jump: jump.wav (triggered on player jump)
     - Collect item: collect.wav (orbs and power-ups)
     - Hit enemy/die: hit.wav (player death)
     - Win game: win.wav (gem collection)
   - ✅ Volume control and enable/disable toggle
   - ✅ Graceful fallback when sound files missing

#### 5. **Visual Polish** - ✅ COMPLETE:
   - ✅ Improved UI fonts (larger, better positioning)
   - ✅ Shadow effects for title and score text (cyberpunk glow)
   - ✅ Dynamic lives color (green → orange → red)
   - ✅ Invincibility indicator with "INVINCIBLE!" text
   - ✅ Purple tint overlay for invincible player sprite
   - ✅ Enhanced menu, win, and game over screens

### Implementation Steps:

✅ **Step 1**: Created `graphics_manager.py` with asset loading
✅ **Step 2**: Updated `entities/player.py` to use loaded sprite
✅ **Step 3**: Updated `entities/enemies.py` to use loaded sprites
✅ **Step 4**: Updated `entities/items.py` to use loaded sprites
✅ **Step 5**: Updated `game_core.py` to integrate background
✅ **Step 6**: Created `sound_manager.py` and integrated sound effects
✅ **Step 7**: Tested all visual and audio elements

### Validation Results:
✅ Game runs at 60 FPS with sprites loaded
✅ Cyberpunk city background displays correctly
✅ Player sprite (64x64) replaces cyan rectangle
✅ All enemy sprites visible with animations (flip on direction change)
✅ All item sprites visible with proper sizes
✅ Sprites maintain transparency (PNG alpha channel)
✅ Sound system functional (graceful fallback when files missing)
✅ No performance degradation with sprites
✅ Fallback to placeholders works if assets missing
✅ Game looks and feels like a complete cyberpunk experience

### Critical Success Criteria for Phase 4:
- ✅ Background image displays correctly
- ✅ Player sprite replaces cyan rectangle
- ✅ All enemy sprites visible and animated
- ✅ All item sprites visible
- ✅ Sprites maintain transparency
- ✅ Sound effects play on key events (ready for audio files)
- ✅ No performance degradation
- ✅ Fallback to placeholders if assets missing
- ✅ Game looks and feels like a complete product

### Time Allocation: 25 minutes total
- Graphics Manager: 5 min
- Sprite Integration: 10 min
- Background: 3 min
- Sound Effects: 5 min
- Polish: 2 min

### Asset Paths Reference:
```
✅ assets/sprites/characters/player.png (64x64)
✅ assets/sprites/characters/spider_robot.png (48x48)
✅ assets/sprites/characters/humanoid_robot.png (64x80)
✅ assets/sprites/characters/flying_vessel.png (56x40)
✅ assets/sprites/items/energy_orb.png (24x24)
✅ assets/sprites/items/power_up.png (32x32)
✅ assets/sprites/items/holographic_gem.png (48x48)
✅ assets/backgrounds/level.png (1536x1024)
✅ assets/backgrounds/splashscreen.png (1536x1024)
⏳ assets/sounds/jump.wav (ready for integration)
⏳ assets/sounds/collect.wav (ready for integration)
⏳ assets/sounds/hit.wav (ready for integration)
⏳ assets/sounds/win.wav (ready for integration)
```

**Note**: Sound files will be automatically loaded when added to the assets/sounds/ directory.

---

## What Happens After Phase 4:

✅ **Phase 4 Complete!** The game is now fully playable with:
- Professional sprite graphics
- Cyberpunk background art
- Audio system (ready for sound files)
- Polished UI and visual effects

### 🚀 Next Steps - Phase 5: Advanced Features (Optional):
- Add menus with mouse support
- Implement difficulty scaling
- Add high score tracking and persistence
- Create multiple levels with progression
- Add particle effects for collectibles
- Implement camera shake on events
- Add background music
- Create level transitions
- Add achievement system

The core game is **production-ready** and can be played end-to-end!

---

## Dependencies Check:
- ✅ Phase 1 complete - Foundation ready
- ✅ Phase 2 complete - All assets generated
- ✅ Phase 3 complete - Gameplay fully functional
- ✅ Phase 4 complete - Graphics and audio integrated!
- 🚀 Phase 5 ready to start - Advanced features next

---

## Current Game Status:

### ✅ Fully Functional Features:
- **Core Gameplay**: Complete platformer with physics
- **Graphics**: All sprites integrated with backgrounds
- **Audio System**: Sound manager ready (awaiting audio files)
- **UI**: Polished menus and HUD with cyberpunk styling
- **Game States**: Menu → Playing → Game Over/Win
- **Lives System**: 3 lives with respawning
- **Scoring**: Points for collectibles (10, 50, 500)
- **Enemies**: 3 types with patrol/movement AI
- **Collectibles**: Energy orbs, power-ups, holographic gem
- **Win Condition**: Collect gem to win
- **Controls**: Full keyboard support (Arrow keys/WASD + Space)

### 🎮 How to Play:
```bash
cd d:\devday-2025\src\game
python main.py
```

**Controls**:
- Arrow Keys / WASD: Move left/right
- SPACE / UP / W: Jump
- R: Restart game
- ESC: Quit

**Objective**: Navigate platforms, avoid enemies, collect the holographic gem!

---

## Quick Reference - Key Pygame Patterns:

### Loading Sprites:
```python
# Load with transparency
sprite = pygame.image.load('path/to/sprite.png').convert_alpha()

# Scale if needed
sprite = pygame.transform.scale(sprite, (width, height))

# Flip horizontally
sprite_flipped = pygame.transform.flip(sprite, True, False)
```

### Loading Sounds:
```python
pygame.mixer.init()
sound = pygame.mixer.Sound('path/to/sound.wav')
sound.play()
```

### Drawing Background:
```python
background = pygame.image.load('path/to/bg.png').convert()
screen.blit(background, (0, 0))  # Draw before sprites
```

---

## Notes for Development Team:

- **Asset paths**: Use relative paths from src/game/ directory
- **Fallback strategy**: Keep colored rectangles if images fail to load
- **Performance**: Cache all loaded images in graphics_manager
- **Sound volume**: Adjust with `sound.set_volume(0.5)` if too loud
- **Test frequently**: Run `python main.py` after each integration step
- **Visual feedback**: Ensure invincibility is clearly visible to player
