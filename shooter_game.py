from game import *

display.set_caption('Шутер')

background = transform.scale(image.load('galaxy.jpg'), WINDOW_SIZE)
clock = time.Clock()

player = Player('rocket.png', WINDOW_SIZE[0] / 2 - Sprite_Size[0] / 2, WINDOW_SIZE[1] - Sprite_Size[1], 5)

mixer.init()
space = mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()

enemies = sprite.Group()

for i in range(1):
    enemies.add(Enemy("asteroid.png", randint(0, WINDOW_SIZE[0] - Sprite_Size[0]), randint(-100, 0), randint(3 , 5), DOWN))

asteroids = sprite.Group()
for i in range(1):
    asteroids.add(Enemy('ufo.png', randint(WINDOW_SIZE[0], WINDOW_SIZE[0] + 100), randint(0, WINDOW_SIZE[1] - (Sprite_Size[1] * 2 - 20)), randint(1, 2), LEFT))
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0,0))

        player.move()
        player.reset()
        player.fire()

        enemies.draw(window)
        enemies.update()
        
        asteroids.draw(window)
        asteroids.update()

        bullets.update()
        bullets.draw(window)

        for enemy in enemies:
            for bullet in bullets:
                if sprite.collide_rect(enemy, bullet):
                    #enemy.kill()

                    enemy.rect.y = 0
                    enemy.rect.x = randint(0, WINDOW_SIZE[0] - Sprite_Size[0])
                    bullet.kill()
                    counter.kill_enemy += 1

                    #enemies.add(Enemy("asteroid.png", randint(0, WINDOW_SIZE[0] - Sprite_Size[0]), randint(-100, 0), randint(3 , 5)))

        counter.show()

        if counter.kill_enemy >= 10:
            finish = True
            window.blit(win, (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
        
        elif counter.lost_enemy >= 5 or sprite.spritecollide(player, enemies, False):
            finish = True
            window.blit(lose, (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))

        display.update()
        clock.tick(FPS)