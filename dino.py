import arcade



class Dino(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()

        self.texture= arcade.load_texture("image\dino g.jpg")

        self.width = 150
        self.height = 150
        self.center_x = w
        self.center_y = h
    
    