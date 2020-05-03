import pygame
from helicopter import Helicopter
from block import Block
import random

pygame.init()

win = pygame.display.set_mode((700,400))
w, h = pygame.display.get_surface().get_size()
bg = pygame.image.load(r'images\finalNight.png')
bg = pygame.transform.scale(bg, (w,h))
clock = pygame.time.Clock()
blocks = []
Font = pygame.font.Font('images\PressStart2P-vaV7.ttf', 16)
smallFont = pygame.font.Font('images\PressStart2P-vaV7.ttf', 10)
score = 0
highScore = 0
explosionSound = pygame.mixer.Sound('images\Explosion.wav')
music = pygame.mixer.music.load('images\music.mp3')
pygame.mixer.music.play(-1)

helicopter = Helicopter(100, 200)

def drawGameWindow():
	win.fill((0,0,0))
	win.blit(bg, (0,0))
	scoreText = Font.render(f"Score: {score}", 1, (255, 255, 255))
	highScoreText = smallFont.render(f"Highscore: {highScore}", 1, (255, 255, 255))
	scoreTextWidth = scoreText.get_width()
	highScoreTextWidth = highScoreText.get_width()
	win.blit(scoreText, (w - 10 - scoreTextWidth, 15))
	win.blit(highScoreText, (w - 10 - highScoreTextWidth, 40))
	helicopter.draw(win)
	if helicopter.alive:
		for block in blocks[:]:
			if block.visible:
				block.draw(win)
			else:
				blocks.remove(block)
	else:
		blocks.clear()
		gameOverMessage = Font.render("GAME OVER...PRESS SPACE TO PLAY AGAIN", 1, (255, 255, 255))
		width, height = gameOverMessage.get_width(), gameOverMessage.get_height()
		win.blit(gameOverMessage, ((w - width) / 2, (h - height) / 2))
	pygame.display.update()

def main():
	run = True
	blockLimiter = 0
	spaceLimiter = 1
	global score
	global highScore
	while run:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()

		if helicopter.alive:
			score += 1
			if blockLimiter > 0:
				blockLimiter +=1
			if blockLimiter > max(50, int(100 - score/10)):
				blockLimiter = 0

			if blockLimiter == 0:
				blocks.append(Block(random.randint(40, h - 100)))
				blockLimiter += 1

			for block in blocks:
				if helicopter.hitbox[1] < block.hitbox[1] + block.hitbox[3] and helicopter.hitbox[1] + helicopter.hitbox[3] > block.hitbox[1]:
					if helicopter.hitbox[0] + helicopter.hitbox[2] > block.hitbox[0] and helicopter.hitbox[0] < block.hitbox[0] + block.hitbox[2]:
						helicopter.hit()
						explosionSound.play()
						for block in blocks:
							block.movable = False

			if helicopter.y >= h or helicopter.y <= 0:
				helicopter.hit()
				explosionSound.play()

			if keys[pygame.K_SPACE]:
				helicopter.y -= abs(helicopter.speed)

			else:
				helicopter.y += helicopter.speed
			if score > highScore:
				highScore = score
		else:
			if spaceLimiter > 0:
				spaceLimiter += 1
			if spaceLimiter > 3:
				spaceLimiter = 0
			if spaceLimiter == 0:
				spaceLimiter += 1
				if keys[pygame.K_SPACE]:
					helicopter.reset()
					score = 0

		drawGameWindow()

	pygame.quit()

main()



