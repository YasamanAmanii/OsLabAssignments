import arcade
import random

SCREEN_WIDTH =700
SCREEN_HEIGHT=700


class Snake(arcade.Sprite) : 
    def __init__(self) :
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.GREEN
        self.ChangeX = None
        self.ChangeY = None
        self.score=0
        self.center_x=SCREEN_WIDTH // 2
        self.center_y=SCREEN_HEIGHT // 2
    
    def move(self) :
        pass
    
    def eat(self,E) : 
        if E == "apple" :
            self.score +=1
        if E == "pear" :
            self.score +=2
        if E == "poo" :
            self.score -=1
    

    def draw(self) :
        arcade.draw_rectangle_filled(self.center_x,self.center_y, self.width,self.height, self.color)

class Apple(arcade.Sprite) : 
    def __init__(self) :
        super().__init__()
        self.image = 'apple.png'
        self.apple = arcade.Sprite(self.image, 0.03)  
        self.apple.center_x=random.randint(10,SCREEN_WIDTH-10)
        self.apple.center_y=random.randint(10,SCREEN_HEIGHT-10)

    def draw(self) :
        self.apple.draw()

class Pear(arcade.Sprite) : 
    def __init__(self) :
        super().__init__()
        self.image = 'pear.png'
        self.pear = arcade.Sprite(self.image, 0.06)  
        self.pear.center_x=random.randint(10,SCREEN_WIDTH-10)
        self.pear.center_y=random.randint(10,SCREEN_HEIGHT-10)

    def draw(self) :
        self.pear.draw()

class Poo(arcade.Sprite) : 
    def __init__(self) :
        super().__init__()
        self.image = 'poo.png'
        self.poo = arcade.Sprite(self.image, 0.05)  
        self.poo.center_x=random.randint(10,SCREEN_WIDTH-10)
        self.poo.center_y=random.randint(10,SCREEN_HEIGHT-10)
    
    def draw(self) :
        self.poo.draw()

class Game(arcade.Window):
    def __init__(self) :
        super().__init__(width=SCREEN_HEIGHT, height=SCREEN_HEIGHT,title="SnakeGame")
        arcade.set_background_color(arcade.color.DARK_GREEN)

        self.snake = Snake()
        self.apple = Apple()
        self.pear = Pear()
        self.poo  =Poo()
    
    
    def on_draw(self) :
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.poo.draw()
        arcade.draw_text('Score = '+ str(self.snake.score),10,10,arcade.color.WHITE,20)
        
        
        
        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.eat("apple")
            self.apple = Apple()
        if arcade.check_for_collision(self.snake, self.pear.pear):
            self.snake.eat("pear")
            self.pear = Pear()
        if arcade.check_for_collision(self.snake, self.poo.poo):
            self.snake.eat("poo")
            self.poo = Poo()


    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT :
            self.snake.center_x -= 16            
        if key == arcade.key.RIGHT :
            self.snake.center_x += 16
        if key == arcade.key.UP :
            self.snake.center_y += 16
        if key == arcade.key.DOWN :
            self.snake.center_y -=16

    
myGame = Game()
arcade.run()
