from kivy.app import App
from kivy.uix.stacklayout import StackLayout 
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.metrics import dp

class StackLayoutWidget(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range(100):
            b = Button(text = str(i+1), size_hint = (None, None), size = (dp(100), dp(100)))
            self.add_widget(b)

class ScrollViewExample(ScrollView):
    pass

class LabApp(App):
    pass

LabApp().run()