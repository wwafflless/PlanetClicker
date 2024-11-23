import sys
import random
import pygame
import math
from pygame.locals import*

pygame.init()

screen = pygame.display.set_mode((750, 650))

FPS = pygame.time.Clock()
FPS.tick(60)

pixel_font = pygame.font.Font("ThaleahFat.ttf", 32)

class Planet():
    def __init__(self, radius, label, color, distance):
        self.radius = radius
        self.label = pixel_font.render(label, True, (0, 255, 255))
        self.color = color

        self.distance = distance
        self.speed = 5
        self.angle = math.radians(270)

        self.circMove() #self.center = (screen.get_width()/2.0 + (self.distance * math.cos(self.angle)), screen.get_height()/2.0 + (self.distance * math.sin(self.angle)))

    def doesCollide(self, toCheck):
        diff = (toCheck[0] - self.center[0], toCheck[1] - self.center[1])
        magnitude = math.hypot(diff[0], diff[1])
        return magnitude <= self.radius #(toCheck[0] > self.center[0] and toCheck[1] > self.center[1] and toCheck[0] < (self.center[0] + self.radius) and toCheck[1] < (self.center[1] + self.radius))

    def circMove(self):
        self.angle = self.angle + math.radians(self.speed)
        self.center = (screen.get_width()/2.0 + (self.distance * math.cos(self.angle)), screen.get_height()/2.0 + (self.distance * math.sin(self.angle)))

    def mouseUpdate(self, mouse):
        return
        #if self.doesCollide(mouse):
            #self.center = (random.randint(0, screen.get_width() - self.radius), -(self.radius + 25))
    def onMouseDown(self, mouse):
        if self.doesCollide(mouse):
            self.circMove()
            #self.angle = self.angle + math.radians(self.speed)
            #self.center = (screen.get_width()/2.0 + (self.distance * math.cos(self.angle)), screen.get_height()/2.0 + (self.distance * math.sin(self.angle)))
        
            
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius)#if self.center[1] > (screen.get_height() + 25):
        #    self.center = (random.randint(0, screen.get_width() - self.radius), -(self.radius + 25))
        surface.blit(self.label, self.center)

#test_text = pixel_font.render("Hello there, beautiful weather today!", True, (255, 255, 255))

NUM_PLANETS = 7

all_planets = []
for i in range(NUM_PLANETS):
    all_planets.append(Planet(10, "", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) , (i+1) * 50))

while True:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for planet in all_planets:
                planet.onMouseDown(mouse)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for planet in all_planets:
                    planet.speed *= 2
            if event.key == pygame.K_DOWN:
                for planet in all_planets:
                    planet.speed /= 2

    keys = pygame.key.get_pressed()
    if(keys[K_SPACE]):
        for planet in all_planets:
            planet.circMove()

    screen.fill((0, 0, 0))
    
    for planet in all_planets:
        planet.mouseUpdate(mouse)
        planet.draw(screen)

    pygame.draw.circle(screen, (255, 130, 10), (screen.get_width()/2.0, screen.get_height()/2.0), 25)

    pygame.display.update()