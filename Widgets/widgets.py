from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class KivyGridLayout(GridLayout):
    mytext = StringProperty("hello!")
    def onclick(self):
        self.mytext = "you clicked"

    def togglebutton(self, toggle):
        if toggle.state == "down":
            toggle.text = "on"
        else:
            toggle.text = "off"

class KivyApp(App):
    pass
KivyApp().run()