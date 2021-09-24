import arcade

class Ground(arcade.AnimatedWalkingSprite):
    def __init__(self,x, y):
        super().__init__()

        self.walk_left_textures = [arcade.load_texture("image\g0.png"),
                                   arcade.load_texture("image\g1.png"),
                                   arcade.load_texture("image\g2.png")]
        self.center_x = x
        self.center_y = y

        # self.width = 1000
        # self.height = 100

        # self.change_x = -4
        # self.change_y =0

        self.speed = 4