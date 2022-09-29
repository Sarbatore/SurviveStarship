import pygame
from random import randint

class Comet(pygame.sprite.Sprite):

  def __init__(self, Game):
    super().__init__()
    self.Game = Game
    
    self.image = pygame.image.load("assets/pictures/comet.png")
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.x = 0 + randint(1, 1000)
    self.rect.y = -self.rect.height

    self.Damage = 10

    self.Speed = randint(4, 8)

  # Comet Despawn
  def Remove(self):
    self.rect.x = 0 + randint(1, 1000)
    self.rect.y = -self.rect.height
    #self.Game.Comet_Group.remove(self) # Not effective

  # Comet Movements
  def Move(self):
    self.rect.y += self.Speed

    for player in self.Game.IsInCollision(self, self.Game.Player_Group):
      self.Remove()
      player.Damaged(self.Damage)

    if self.rect.y + self.rect.h > 1080:
      self.Remove()