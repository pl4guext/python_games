# coding=utf-8




class env_variables:

    def __init__(self):
        self.width = 600
        self.height = 400
        self.window_size = (self.width, self.height)
        self.center_x = self.width * 0.5
        self.center_y = self.height * 0.5


class game_variables:

    def __init__(self):
        self.x_speed = 10
        self.y_speed = 10
        self.object_w = 50
        self.object_h = 75
        self.object_size = (self.object_w, self.object_h)
        self.ball_rad = 10
        self.x_speed_ball = 3
        self.y_speed_ball = 3
        
