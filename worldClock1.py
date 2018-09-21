import pygame
import time
import math
import maths

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

winWidth = winHeight = 600

pygame.init()
clock = pygame.time.Clock()
clockDisplay = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Analog Clock")
clockImg = pygame.image.load('clock.png')
clockImg = pygame.transform.scale(clockImg,(winWidth, winHeight))


def clockRunning():
	clockRun = False	
	c1, d1 = maths.minutes[int(maths.mm%60)-16]
	c2, d2 = maths.hours[int(maths.hh%360)]
	secs = mins = hrs = 0
	while not clockRun:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		c, d = maths.seconds[(maths.ss%60)-16]
		
		clockDisplay.fill(black)
		clockDisplay.blit(clockImg, (0, 0))
		secHand = pygame.draw.line(clockDisplay, black, (maths.h, maths.k), (c, d), 3)
		minHand = pygame.draw.line(clockDisplay, black, (maths.h, maths.k), (c1, d1), 5)
		hourHand = pygame.draw.line(clockDisplay, black, (maths.h, maths.k), (c2, d2), 10)
		
		pygame.display.update()
		time.sleep(1)

		maths.ss+=1
		secs += 1

		if secs == 60:
			secs = 0
			mins += 1
			if mins % 2 == 0:
				if mins == 60:
					mins = 0
					hrs += 1
				maths.hh += 1
				c2, d2 = maths.hours[(maths.hh%360)]

			maths.mm += 1
			c1, d1 = maths.minutes[(maths.mm%60)-16]
			
		
		pygame.display.update()
		clock.tick(30)

clockRunning()

pygame.quit()
quit()