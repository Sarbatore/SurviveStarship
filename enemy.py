import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):

  def __init__(self, Game):
    super().__init__()
    self.Game = Game
    
    self.image = pygame.image.load("assets/pictures/battleship.png")
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.x = 0 + randint(1, 1000)
    self.rect.y = 0 + randint(1, 50)

    self.Health = 100
    self.MaxHealth = 100
    self.Damage = 10
    
    self.Direction = randint(1, 2)
    self.Speed = randint(2, 8)

  # Respawn
  def Remove(self):
    for player in self.Game.Player_Group:
      player.Kills += 1
      
    self.rect.x = 0 + randint(1, 1000)
    self.rect.y = 0 + randint(1, 50)
    self.Health = self.MaxHealth
    #self.Game.Enemy_Group.remove(self) # Not effective

  # Get Damaged
  def Damaged(self, amount):
    self.Health -= amount

    if self.Health <= 0:
      self.Remove()

  def ReCoordonateLeft(self):
    self.Direction = 2

  def ReCoordonateRight(self):
    self.Direction = 1

  # Movements
  def Move(self):
    if self.Direction == 1:
      if self.rect.x + self.rect.w + self.Speed >= 1080:
        self.ReCoordonateLeft()
      else:
        self.rect.x += self.Speed

    else:
      if self.rect.x - self.Speed <= 10:
        self.ReCoordonateRight()
      else:
        self.rect.x -= self.Speed

    # Respawn when hits player
    for player in self.Game.IsInCollision(self, self.Game.Player_Group):
      self.Remove()
      player.Damaged(self.Damage)

  # Update Enemy Health Bar
  def update_health(self, surface):
    # Back
    health_back_color = (60, 63, 60)
    health_back_position = [self.rect.x, self.rect.y, self.MaxHealth, 5]
    pygame.draw.rect(surface, health_back_color, health_back_position)
    # Health
    health_color = (111, 210, 46)
    health_position = [self.rect.x, self.rect.y, self.Health, 5]
    pygame.draw.rect(surface, health_color, health_position)