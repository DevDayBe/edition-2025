"""
Game Core - Main game loop and state management
"""
from enum import Enum

import pygame
from pydantic import BaseModel

from entities.enemies import create_level_enemies
from entities.items import create_level_items
from entities.platform import create_level_platforms
from entities.player import Player
from entities.boss import create_boss
from sound_manager import SoundManager
from graphics_manager import GraphicsManager


class GameState(str, Enum):
    """Game state enumeration."""
    MENU = "menu"
    PLAYING = "playing"
    GAME_OVER = "game_over"
    WIN = "win"


class GameData(BaseModel):
    """Game data model using pydantic."""
    score: int = 0
    lives: int = 3
    state: GameState = GameState.MENU

    class Config:
        use_enum_values = True


class GameCore:
    """Main game logic and state management."""

    def __init__(self, screen: pygame.Surface):
        """
        Initialize game core.

        Args:
            screen: Pygame display surface
        """
        self.screen = screen
        self.data = GameData()

        # Initialize managers
        self.graphics_manager = GraphicsManager()
        self.sound_manager = SoundManager()

        # Create level elements
        self.platforms = create_level_platforms()
        self.enemies = create_level_enemies(self.graphics_manager)
        self.energy_orbs, self.powerups, self.gem = create_level_items(self.graphics_manager)

        # Create boss
        self.boss = create_boss(self.graphics_manager)
        self.boss_group = pygame.sprite.GroupSingle(self.boss)
        self.boss_defeated = False

        # Create player (start on ground platform, left side)
        player_sprite = self.graphics_manager.get_sprite('player')
        self.player = Player(50, 581, player_sprite)  # y = 645 (ground) - 64 (player height)
        self.player.sound_manager = self.sound_manager
        self.player_group = pygame.sprite.GroupSingle(self.player)

        # Gem group for collision detection
        self.gem_group = pygame.sprite.GroupSingle(self.gem)

        # Respawn position (on ground platform)
        self.respawn_x = 50
        self.respawn_y = 581

        # Death timer
        self.death_timer = 0

    def update(self):
        """Update game state."""
        if self.data.state == GameState.MENU:
            # Check for space to start
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.data.state = GameState.PLAYING
                print("Game started!")

        elif self.data.state == GameState.PLAYING:
            # Update player
            self.player.update(self.platforms)

            # Update enemies
            self.enemies.update()

            # Update boss
            if not self.boss_defeated:
                self.boss.update()

            # Check if player fell off screen
            if self.player.rect.top > 1024:
                self.player_death()

            # Check collisions with enemies
            if not self.player.invincible:
                enemy_hits = pygame.sprite.spritecollide(
                    self.player, self.enemies, False)
                if enemy_hits:
                    self.player_death()
                    print("Player hit by enemy!")

            # Check collision with boss
            if not self.boss_defeated:
                boss_hit = pygame.sprite.spritecollide(
                    self.player, self.boss_group, False)
                if boss_hit:
                    # Player with invincibility can damage boss
                    if self.player.invincible:
                        if self.boss.take_damage():
                            self.boss_defeated = True
                            self.boss_group.empty()
                            self.data.score += 200  # Bonus for defeating boss
                            self.sound_manager.play('hit')
                            print("Boss defeated! +200 points")
                    else:
                        # Boss damages player (only if player not invincible)
                        self.player_death()
                        print("Player hit by boss!")

            # Check collisions with energy orbs
            orb_hits = pygame.sprite.spritecollide(
                self.player, self.energy_orbs, True)
            for orb in orb_hits:
                self.data.score += orb.points
                self.sound_manager.play('collect')
                print(f"Collected energy orb! +{orb.points} points")

            # Check collisions with powerups
            powerup_hits = pygame.sprite.spritecollide(
                self.player, self.powerups, True)
            for powerup in powerup_hits:
                self.data.score += powerup.points
                self.player.activate_powerup()
                self.sound_manager.play('collect')
                print(f"Collected powerup! +{powerup.points} points")

            # Check collision with gem (win condition - only if boss defeated)
            if self.boss_defeated:
                gem_hit = pygame.sprite.spritecollide(
                    self.player, self.gem_group, True)
                if gem_hit:
                    self.data.score += self.gem.points
                    self.data.state = GameState.WIN
                    self.sound_manager.play('win')
                    print(
                    f"Collected holographic gem! You win! +{self.gem.points} points")

            # Handle death timer
            if self.death_timer > 0:
                self.death_timer -= 1
                if self.death_timer == 0:
                    self.respawn_player()

        elif self.data.state == GameState.GAME_OVER:
            # Check for R to restart
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.restart_game()

        elif self.data.state == GameState.WIN:
            # Check for R to restart
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.restart_game()

    def player_death(self):
        """Handle player death."""
        self.data.lives -= 1
        self.sound_manager.play('hit')
        print(f"Player died! Lives remaining: {self.data.lives}")

        if self.data.lives <= 0:
            self.data.state = GameState.GAME_OVER
            print("Game Over!")
        else:
            self.death_timer = 60  # 1 second delay before respawn

    def respawn_player(self):
        """Respawn player at starting position."""
        self.player.reset_position(self.respawn_x, self.respawn_y)
        print("Player respawned")

    def restart_game(self):
        """Restart the game."""
        # Reset game data
        self.data = GameData()

        # Recreate level elements
        self.platforms = create_level_platforms()
        self.enemies = create_level_enemies(self.graphics_manager)
        self.energy_orbs, self.powerups, self.gem = create_level_items(self.graphics_manager)
        self.gem_group = pygame.sprite.GroupSingle(self.gem)

        # Recreate boss
        self.boss = create_boss(self.graphics_manager)
        self.boss_group = pygame.sprite.GroupSingle(self.boss)
        self.boss_defeated = False

        # Reset player
        self.player.reset_position(self.respawn_x, self.respawn_y)
        self.player.invincible = False
        self.player.invincible_timer = 0

        self.death_timer = 0
        print("Game restarted!")

    def draw(self):
        """Draw game elements."""
        # Get background
        background = self.graphics_manager.get_background('level')
        
        if background:
            # Draw background image
            self.screen.blit(background, (0, 0))
        else:
            # Fallback to dark color if background not loaded
            self.screen.fill((10, 10, 30))
        
        if self.data.state == GameState.MENU:
            # Draw menu with cyberpunk styling
            font_title = pygame.font.Font(None, 96)
            font_subtitle = pygame.font.Font(None, 48)
            font_text = pygame.font.Font(None, 36)

            # Title with glow effect (render twice with offset)
            title_shadow = font_title.render("CYBERPUNK RACER", True, (0, 100, 100))
            title = font_title.render("CYBERPUNK RACER", True, (0, 255, 255))
            
            start_text = font_subtitle.render("Press SPACE to Start", True, (255, 255, 255))
            controls = font_text.render("Arrow Keys / WASD to Move, SPACE to Jump", True, (150, 150, 200))
            
            # Additional instructions
            objective = font_text.render("Collect the Holographic Gem to Win!", True, (100, 255, 100))

            # Center all text
            title_rect = title.get_rect(center=(768, 280))
            title_shadow_rect = title_shadow.get_rect(center=(770, 282))
            start_rect = start_text.get_rect(center=(768, 450))
            controls_rect = controls.get_rect(center=(768, 550))
            objective_rect = objective.get_rect(center=(768, 620))

            # Draw shadow first
            self.screen.blit(title_shadow, title_shadow_rect)
            self.screen.blit(title, title_rect)
            self.screen.blit(start_text, start_rect)
            self.screen.blit(controls, controls_rect)
            self.screen.blit(objective, objective_rect)

        elif self.data.state == GameState.PLAYING:
            # Draw platforms
            self.platforms.draw(self.screen)

            # Draw enemies
            self.enemies.draw(self.screen)

            # Draw boss (if not defeated)
            if not self.boss_defeated:
                self.boss_group.draw(self.screen)

            # Draw items
            self.energy_orbs.draw(self.screen)
            self.powerups.draw(self.screen)
            self.gem_group.draw(self.screen)

            # Draw player (unless in death timer)
            if self.death_timer == 0:
                self.player_group.draw(self.screen)

            # Draw UI with cyberpunk styling
            font_score = pygame.font.Font(None, 48)
            font_lives = pygame.font.Font(None, 48)
            
            # Score with glow effect
            score_shadow = font_score.render(f"SCORE: {self.data.score}", True, (0, 100, 100))
            score_text = font_score.render(f"SCORE: {self.data.score}", True, (0, 255, 255))
            
            # Lives with color based on count
            lives_color = (0, 255, 0) if self.data.lives > 1 else (255, 100, 0) if self.data.lives == 1 else (255, 0, 0)
            lives_text = font_lives.render(f"LIVES: {self.data.lives}", True, lives_color)

            # Draw with shadow effect
            self.screen.blit(score_shadow, (22, 22))
            self.screen.blit(score_text, (20, 20))
            self.screen.blit(lives_text, (20, 70))
            
            # Invincibility indicator
            if self.player.invincible:
                font_inv = pygame.font.Font(None, 36)
                inv_text = font_inv.render("INVINCIBLE!", True, (255, 0, 255))
                self.screen.blit(inv_text, (20, 130))
            
            # Boss health indicator (if boss not defeated)
            if not self.boss_defeated:
                font_boss = pygame.font.Font(None, 42)
                boss_health_text = font_boss.render(f"BOSS: {'█' * self.boss.health}{'░' * (self.boss.max_health - self.boss.health)}", True, (255, 69, 0))
                self.screen.blit(boss_health_text, (20, 180))

        elif self.data.state == GameState.GAME_OVER:
            # Draw game over screen with cyberpunk styling
            font_title = pygame.font.Font(None, 96)
            font_text = pygame.font.Font(None, 54)
            font_restart = pygame.font.Font(None, 42)

            # Title with pulsing red effect
            game_over_shadow = font_title.render("GAME OVER", True, (100, 0, 0))
            game_over = font_title.render("GAME OVER", True, (255, 50, 50))
            
            final_score = font_text.render(f"Final Score: {self.data.score}", True, (255, 255, 255))
            restart = font_restart.render("Press R to Restart", True, (200, 200, 200))

            # Center all text
            game_over_rect = game_over.get_rect(center=(768, 380))
            game_over_shadow_rect = game_over_shadow.get_rect(center=(770, 382))
            score_rect = final_score.get_rect(center=(768, 500))
            restart_rect = restart.get_rect(center=(768, 600))

            self.screen.blit(game_over_shadow, game_over_shadow_rect)
            self.screen.blit(game_over, game_over_rect)
            self.screen.blit(final_score, score_rect)
            self.screen.blit(restart, restart_rect)

        elif self.data.state == GameState.WIN:
            # Draw win screen with celebratory styling
            font_title = pygame.font.Font(None, 96)
            font_text = pygame.font.Font(None, 54)
            font_restart = pygame.font.Font(None, 42)

            # Title with green glow
            win_shadow = font_title.render("YOU WIN!", True, (0, 100, 0))
            win_text = font_title.render("YOU WIN!", True, (0, 255, 100))
            
            final_score = font_text.render(f"Final Score: {self.data.score}", True, (255, 255, 255))
            restart = font_restart.render("Press R to Play Again", True, (200, 200, 200))

            # Center all text
            win_rect = win_text.get_rect(center=(768, 380))
            win_shadow_rect = win_shadow.get_rect(center=(770, 382))
            score_rect = final_score.get_rect(center=(768, 500))
            restart_rect = restart.get_rect(center=(768, 600))

            self.screen.blit(win_shadow, win_shadow_rect)
            self.screen.blit(win_text, win_rect)
            self.screen.blit(final_score, score_rect)
            self.screen.blit(restart, restart_rect)
