from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

class KivyGridLayout(GridLayout):
    mytext = StringProperty("hello!")
    button_disabled = BooleanProperty(False)

    def onclick(self):
        self.mytext = "you clicked"

    def togglebutton(self, toggle):
        if toggle.state == "down":
            toggle.text = "on"
            self.button_disabled = True
        else:
            toggle.text = "off"
            self.button_disabled = False

    def switchbehaviour(self, switch):
        print("Switch: " + str(switch.active))
class KivyApp(App):
    pass
KivyApp().run()