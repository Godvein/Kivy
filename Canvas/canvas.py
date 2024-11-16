from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.metrics import dp
from kivy.properties import Clock

class CanvasWidget(Widget):
    pass
class CanvasWidget1(Widget):
    pass

class CanvasWidget2(Widget):
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        with self.canvas:
            Line(points = (0,0, 100,300), width = 2)
            Color(rgb = (0,1,0))
            Line(circle = (100,100, 50), width = 2)
            self.rect = Rectangle(pos = (0, 350), size = (100,100))

    def move(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        
        diff = self.width - (x+w) #logic to keep rectangle inside the border 
        if diff < inc:
            inc = diff

        x += inc

        self.rect.pos=(x, y)

class CanvasWidget3(Widget):
    def __init__(self, **kwargs):
        self.ball_size = dp(50)
        self.velocity_x = dp(4)
        self.velocity_y = dp(5)
        super().__init__(**kwargs)
        with self.canvas:
            self.ball = Ellipse(pos = self.center, size = (self.ball_size,self.ball_size))
            Clock.schedule_interval(self.update, 1/60)

    #called whenever the screen is resized    
    def on_size(self, *args):
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    #called every frame
    def update(self, dt):
        x, y = self.ball.pos

        x += self.velocity_x
        y +=self.velocity_y

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.velocity_x = -self.velocity_x

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.velocity_y = -self.velocity_y
        self.ball.pos = (x,y)
        
        if x < 0:
            x = 0
            self.velocity_x = -self.velocity_x

        if y < 0:
            y = 0
            self.velocity_y = -self.velocity_y
class CanvasApp(App):
    pass


CanvasApp().run()