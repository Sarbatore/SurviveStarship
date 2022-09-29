import pygame
from player import Player
from comet import Comet
from enemy import Enemy

class Game:

  def __init__(self):
    # Player Managements
    self.Player_Group = pygame.sprite.Group()
    self.Player = Player(self)
    self.Player_Group.add(self.Player)

    # Keys Pressed
    self.Pressed = {}
    
    # Comet Managements
    self.Comet_Group = pygame.sprite.Group()
    for i in range(0,5):
      self.Spawn_Comet()

    # Enemies Managements
    self.Enemy_Group = pygame.sprite.Group()
    for i in range(0,3):
      self.Spawn_Enemy()

  # Collision Between 2 entities
  def IsInCollision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

  # Spawn a Comet in the World
  def Spawn_Comet(self):
    self.Comet_Group.add(Comet(self))

  # Spawn an Enemy in the World
  def Spawn_Enemy(self):
    self.Enemy_Group.add(Enemy(self))
