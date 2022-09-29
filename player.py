from ctypes.wintypes import RGB
import pygame
from missile import Missile
from sys import exit

white = (255, 255, 255)
green = (7, 200, 75)
blue = (69, 90, 185)
black = (0, 0, 0)

class Player(pygame.sprite.Sprite):

  def __init__(self, Game):
    super().__init__()
    self.Game = Game
    self.image = pygame.image.load("assets/pictures/spaceship.png")
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.x = 540 - (self.rect.w/2) - 10
    self.rect.y = 720 - self.rect.h - 10

    self.Health = 100
    self.MaxHealth = 100
    
    self.Kills = 0

    self.IsInNitro = False
    self.NitroSpeed = 5
    self.Stamina = 100 #Not Used
    self.MaxStamina = 100 #Not Used

    self.IsMoving = False
    self.OrgSpeed = 10
    self.Speed = self.OrgSpeed
    
    self.Damage = 20
    self.Missile_Group = pygame.sprite.Group()

  # Player Despawn
  def Remove(self):
    self.Game.Player_Group.remove(self)
  
  # Player Get Damaged
  def Damaged(self, amount):
    self.Health -= amount

    # Game Finished when Die
    if self.Health <= 0:
      self.Remove()
      pygame.quit()
      exit()

  # Player Move Up
  def MoveUp(self):
    self.rect.y -= self.Speed

  # Player Move Down
  def MoveDown(self):
    self.rect.y += self.Speed

  # Player Move Right
  def MoveRight(self):
    self.rect.x += self.Speed

  # Player Move Left
  def MoveLeft(self):
    self.rect.x -= self.Speed

  # Player Shoots
  def Shoot(self):
    self.Missile_Group.add(Missile(self))

  # Enable Player Nitro
  def Nitro(self):
    self.IsInNitro = True
    self.Speed += self.NitroSpeed

  # Stop Player Nitro
  def StopNitro(self):
    self.IsInNitro = False
    self.Speed = self.OrgSpeed

  # Update Player Health Bar
  def update_health(self, surface):
    # Back
    health_back_color = (60, 63, 60)
    health_back_position = [self.rect.x, self.rect.y + self.rect.h, self.MaxHealth, 5]
    pygame.draw.rect(surface, health_back_color, health_back_position)
    # Health
    health_color = (111, 210, 46)
    health_position = [self.rect.x, self.rect.y + self.rect.h, self.Health, 5]
    pygame.draw.rect(surface, health_color, health_position)

  # Update Player Kills
  def update_kills(self, surface):
    font = pygame.font.SysFont("Ariel", 48)
    img = font.render("Kills: " + str(self.Kills), True, white, green)
    rect = img.get_rect()
    rect.left = 0
    rect.bottom = 720
    surface.blit(img, rect)