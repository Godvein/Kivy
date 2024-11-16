from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *

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
class CanvasApp(App):
    pass


CanvasApp().run()