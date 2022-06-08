import random,time,math,arcade

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed = 8
        self.angle = host.angle 
        self.center_x = host.center_x
        self.center_y = host.center_y
    def move(self):
        angle_radious = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_radious)
        self.center_y += self.speed * math.cos(angle_radious)
    def launch(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser1.wav'), 0.2, 0.0,False)
    
class Enemy(arcade.Sprite):
    def __init__(self, w, h ,speed=3):
        super().__init__('Enemy.png')
        self.speed = speed
        self.center_x = random.randint(0, w)
        self.center_y = h+10 
        self.angle = 0
        self.width = 50
        self.height = 50
    def move(self):
        self.center_y -= self.speed  
    def hit(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/hit3.wav'), 1.0, 0.0,False)

class PlayerShip(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__('PlayerShip.png')
        self.width = 48
        self.height = 48
        self.center_x = w//2
        self.center_y = 48
        self.change_x = 0
        self.change_y = 0
        self.angle = 0
        self.ChangeAngle = 0
        self.BulletList = []
        self.speed = 8
        self.score = 0
        self.health = 3
    def rotate(self):
        self.angle += self.ChangeAngle * self.speed
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
    def fire(self):
        self.BulletList.append(Bullet(self))
     
class Game(arcade.Window):
    
    def __init__(self):
        self.w = 700
        self.h = 700
        super().__init__(self.w, self.h, title="BatlleShip Game")
        self.BackgroundImage = arcade.load_texture('Background.jpg')
        self.HealthImage = arcade.load_texture('Heart.png')
        self.Ship = PlayerShip(self.w, self.h)
        self.enemy = Enemy(self.w, self.h)
        self.NextEnemy = random.randint(1,3)
        self.EnemyList = []
        self.GameStart = time.time()
        self.Start = time.time()
        
        


    def on_draw(self):
        arcade.start_render()
        if self.Ship.health <=0 :
            arcade.draw_text('GAME OVER !!!! :(', self.w//2-200, self.h//2, arcade.color.WHITE, 40 //2, width=400, align='center')
            score = "Score = " + str(self.Ship.score)
            arcade.draw_text(score, self.w//2-200, self.h//2-100, arcade.color.WHITE, 40 //2, width=400, align='center')
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.BackgroundImage)  
            self.Ship.draw()
            for i in range(len(self.Ship.BulletList)):
                self.Ship.BulletList[i].draw()

            for i in range(len(self.EnemyList)):
                self.EnemyList[i].draw()

            for i in range(self.Ship.health):
                arcade.draw_lrwh_rectangle_textured(10+i*35 ,10 ,30 ,30 ,self.health_image)
            arcade.draw_text('Score: %i'%self.Ship.score, self.w-130, 10, arcade.color.WHITE, 40 //2, width=200, align='left')


    def on_update(self, delta_time):
        self.End = time.time()
        if self.Ship.score%10 == 0 and self.Ship.score >=10:
            self.enemy.speed +=1
        if self.End - self.Start > self.NextEnemy:
            self.NextEnemy = random.randint(1, 3)
            self.EnemyList.append(Enemy(self.w, self.h, 3+(self.End-self.GameStart)//24))
            self.Start = time.time()
        self.Ship.rotate()
        self.Ship.move()
        for i in range(len(self.Ship.BulletList)):
            self.Ship.BulletList[i].move()

        for i in range(len(self.EnemyList)):
            self.EnemyList[i].move()
        for enemy in self.EnemyList:
            for bullet in self.Ship.BulletList:

                if arcade.check_for_collision(bullet, enemy):
                    enemy.hit()
                    self.Ship.BulletList.remove(bullet)
                    self.EnemyList.remove(enemy)
                    self.Ship.score += 1
        for enemy in self.EnemyList:
            if enemy.center_y < 0:
                self.Ship.health -= 1
                self.EnemyList.remove(enemy)
        for bullet in self.Ship.BulletList:
          if bullet.center_y>self.height or bullet.center_x<0 or bullet.center_x>self.width:
                self.Ship.BulletList.remove(bullet)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.Ship.change_x = 1
        elif key == arcade.key.LEFT:
            self.Ship.change_x = -1
        elif key == arcade.key.UP:
            self.Ship.change_y = 1
        elif key == arcade.key.DOWN:
            self.Ship.change_y = -1
        elif key == arcade.key.C:
            self.Ship.ChangeAngle = 1
        elif key == arcade.key.V:
            self.Ship.ChangeAngle = -1           
        elif key == arcade.key.SPACE:
            self.Ship.fire()
            self.Ship.BulletList[-1].launch()
    def on_key_release(self, key, modifiers):
        self.Ship.ChangeAngle = 0
        self.Ship.change_x = 0
        self.Ship.change_y = 0
Game()
arcade.run()