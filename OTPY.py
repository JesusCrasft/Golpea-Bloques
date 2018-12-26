import pygame
import random
pygame.init()
sonido1 = pygame.mixer.Sound("img/Crash.mp3")
pantalla = pygame.display.set_mode((480,500))
salir = False
relog1 = pygame.time.Clock()
fuente1 = pygame.font.SysFont("Arial", 20, True, False)
info = fuente1.render("Tienes 10 segundos", 0, (255,255,255))
gris = (145,145,145)
blanco = (255,255,255)
negro = (0,0,0)
listarec = []
segundosint = 0
termino = False
rotos = 0
r1 = pygame.Rect(0,0,10,10)
for x in range(25):
	w = random.randrange(5,25)
	h = random.randrange(5,25)
	x = random.randrange(450)
	y = random.randrange(450)
	listarec.append(pygame.Rect(x,y,w,h))

while salir != True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			for recs in listarec:
				if termino == False:
					if r1.colliderect(recs):
						sonido1.play()
						recs.width = 0
						recs.height = 0
						rotos += 1

	relog1.tick(20)
	(r1.left,r1.top) = pygame.mouse.get_pos()
	r1.left -= r1.width/2
	r1.top -= r1.height/2
	pantalla.fill(gris)
	for recs in listarec:
		pygame.draw.rect(pantalla,blanco,recs)
	pygame.draw.rect(pantalla,negro,r1)	
	pantalla.blit(info,(5,5))
	if segundosint >= 10:
			termino = True
	if termino == False:
		segundosint = pygame.time.get_ticks()/1000
		segundos = str(segundosint)
		contador = fuente1.render(segundos,0,(0,0,230))
	else:
		contador = fuente1.render(segundos+" Usted rompio: "+str(rotos),0,(0,0,230))
	pantalla.blit(contador,(250,5))
	pygame.display.update()

pygame.quit()	