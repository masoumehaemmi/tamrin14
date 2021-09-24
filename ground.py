import arcade

class Ground(arcade.AnimatedWalkingSprite):
    def __init__(self,width, height):
        super().__init__()

        self.walk_left_textures = [arcade.load_texture("image\ground0.jpg"),
                                   arcade.load_texture("image\ground1.jpg"),
                                   arcade.load_texture("image\ground2.jpg")]
        self.center_x = width
        self.center_y = height

        self.width = 50
        self.height = 50

        self.change_x = -4
        self.change_y =0

        self.speed = 4