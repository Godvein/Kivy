from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.metrics import dp

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
        
        
class CanvasApp(App):
    pass


CanvasApp().run()