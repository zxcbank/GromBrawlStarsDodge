import random
import pygame
import Constants
import Player
import other
import time
import matplotlib.pyplot as plt

'''import myPlayer
import myStrikes

'''

# Default
pygame.init()
screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption("Brawl Training")
clock = pygame.time.Clock()
screen.fill(Constants.BLACK)

#создание групп 2D объектов
all_sprites = pygame.sprite.Group()
all_spikes = pygame.sprite.Group()

#начальные объекты
brawler = Player.Player()
all_sprites.add(brawler)

# игровой цикл
running = True
now = startTime = time.time()
all_sprites.draw(screen)

#фан для статистики
timelist = []
quantlist = []
while running:
    timelist.append(int((now - startTime)))
    quantlist.append(len(all_spikes))
    # default в игровом цикле
    clock.tick(Constants.FPS)
    #генерация новых частиц
    if time.time() - 0.5 > now:
        quantity = random.randint(2, 4)  # количество ежесекундно добьавляющихся молний
        now = time.time()
        for i in range(quantity + 1):
            other.generator(all_spikes)

    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    all_spikes.update(all_spikes)

    #рендер
    screen.fill(Constants.BLACK)
    all_sprites.draw(screen)
    all_spikes.draw(screen)
    pygame.display.flip()

    #столкновения
    for _ in all_spikes:
        if other.breakout(_.rect.x, _.rect.y, brawler.rect.x, brawler.rect.y):
            all_sprites.remove(brawler)
            all_spikes.remove(all)
            running = False
            print(now - startTime, 'seconds')

plt.title('quantity of spikes')
plt.plot(timelist, quantlist)
plt.show()
pygame.quit()