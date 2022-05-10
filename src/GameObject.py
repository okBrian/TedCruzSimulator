class GameObject:
    def __init__(self, image, pos):
        self.image = image
        self.pos = image.get_rect().move(pos)