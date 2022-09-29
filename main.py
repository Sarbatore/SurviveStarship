import pygame
from game import Game
from sys import exit

#pygame.init() #It is too Slow to load !

# Music
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/game.mp3")
pygame.mixer.music.set_volume(0.05)
#pygame.mixer.music.play()

w, h = 1080, 720

pygame.display.set_caption("Survive Starship")
screen = pygame.display.set_mode((w, h))
background = pygame.image.load("assets/pictures/background.jpg")
clock = pygame.time.Clock()

game = Game()

# Toggle Player Nitro
def CanNitro():
  if not game.Player.IsInNitro and game.Pressed.get(pygame.K_LSHIFT):
    game.Player.Nitro()
  elif game.Player.IsInNitro and not game.Pressed.get(pygame.K_LSHIFT):
    game.Player.StopNitro()

while True:
  for event in pygame.event.get():
    # Leave the Game
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

   # Keys when Down
    elif event.type == pygame.KEYDOWN:
      game.Pressed[event.key] = True

      # Shoot when Space Down
      if event.key == pygame.K_SPACE:
        game.Player.Shoot()

   # Keys when UP
    elif event.type == pygame.KEYUP:
      game.Pressed[event.key] = False

  # Player and Background image
  screen.blit(background, (0, 0))
  screen.blit(game.Player.image, game.Player.rect)

  # Health Bars
  game.Player.update_health(screen)
  game.Player.update_kills(screen)

  # Missiles Loop Management
  for missile in game.Player.Missile_Group:
    missile.Move()

  # Comets Loop Management
  for comet in game.Comet_Group:
    comet.Move()

  # Enemy Loop Management
  for enemy in game.Enemy_Group:
    enemy.Move()
    enemy.update_health(screen)

  # Draw Missiles and Comets
  game.Player.Missile_Group.draw(screen)
  game.Comet_Group.draw(screen)
  game.Enemy_Group.draw(screen)

  # Player Movements by X
  if game.Pressed.get(pygame.K_RIGHT) and not game.Pressed.get(pygame.K_LEFT) and game.Player.rect.x < screen.get_width() - game.Player.rect.w - 10:
    game.Player.MoveRight()
    CanNitro()
  elif game.Pressed.get(pygame.K_LEFT) and not game.Pressed.get(pygame.K_RIGHT) and game.Player.rect.x > 10:
    game.Player.MoveLeft()
    CanNitro()

  # Player Movements by Y
  if game.Pressed.get(pygame.K_UP) and not game.Pressed.get(pygame.K_DOWN) and game.Player.rect.y > 0:
    game.Player.MoveUp()
    CanNitro()
  elif game.Pressed.get(pygame.K_DOWN) and not game.Pressed.get(pygame.K_UP) and game.Player.rect.y < screen.get_height() - game.Player.rect.h - 10:
    game.Player.MoveDown()
    CanNitro()


  # Update Screen
  pygame.display.update()
  clock.tick(60)

