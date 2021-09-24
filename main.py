
import arcade
from ground import Ground
from dino import Dino
from bird import Bird

class Game(arcade.Window):
    def __init__(self):
        self.w = 1000
        self.h = 500
        self.gravity = 0.5
        super().__init__(self.w,self.h, "T_Rex Game Saeideh")
        self.color = arcade.color.WHITE
        self.ground_list = arcade.SpriteList()
        self.dino = Dino(self.width,self.height)
        
        for i in range(self.w, self.h):
            ground = Ground(i ,100)
            self.ground_list.append(ground)
        
        self.bird_speed = -5
        self.bird_list = arcade.SpriteList()
        
        for i in range(self.w,self.h):
            bird = Bird(i, 400)
            self.bird_list.append(bird)

        self.cloud = arcade.Sprite("image\cloud.jpg")
        self.cloud.center_x = 900
        self.cloud.center_y = 130
        self.cloud.width = 50
        self.cloud.height = 50
        
        self.physics_engine = arcade.PhysicsEnginePlatformer( self.dino,self.ground_list, self.gravity)

def on_draw(self, w, h):
    arcade.start_render()
    arcade.draw_lrwh_rectangle_textured(self.w,self.h,self.color)

    self.dino.draw()
    self.bird.draw()
    self.cloud.draw()
    
    for ground in self.ground_list:
            ground.draw()   
    
    for bird in self.bird_list:
            bird.draw()

def on_update(self,delta_time:float):

    self.physics_engine.update()

    for ground in self.ground_list:
            ground.update()

    for bird in self.bird_list:
            bird.update()

def on_key_press(self, key, modifiers):
    if key == arcade.key.RIGHT:
        self.ground.change_x = 1

game= Game()
arcade.run()
