from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class KivyGridLayout(GridLayout):
    mytext = StringProperty("hello!")
    def onclick(self):
        self.mytext = "you clicked"

class KivyApp(App):
    pass
KivyApp().run()