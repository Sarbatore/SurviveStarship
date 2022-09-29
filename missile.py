from random import randint
import pygame

class Missile(pygame.sprite.Sprite):

  def __init__(self, Player):
    super().__init__()
    self.Player = Player

    # Choice Missile Pos
    pos = randint(1,2)
    
    self.image = pygame.image.load("assets/pictures/missile.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = pos == 1 and Player.rect.x or Player.rect.x + (Player.rect.w / 2)
    self.rect.y = Player.rect.y - 10
    
    self.Speed = 20

  # Missile Despawn
  def Remove(self):
    self.Player.Missile_Group.remove(self)

  # Missile Movements
  def Move(self):
    self.rect.y -= self.Speed

    # Collision with enemies
    for enemy in self.Player.Game.IsInCollision(self, self.Player.Game.Enemy_Group):
      self.Remove()
      enemy.Damaged(self.Player.Damage)

    # Collision with comets
    for comet in self.Player.Game.IsInCollision(self, self.Player.Game.Comet_Group):
      self.Remove()

    # Missile out of map
    if self.rect.y < 0:
      self.Remove()
