from kivy.app import App
from kivy.metrics import dp
from kivy.properties import Clock, BooleanProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window
import random
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen



class GameWidget(Widget):
    def __init__(self, **kwargs):
        #points
        self.points = 0
        self.point_size = dp(50)

        #tank
        self.tank_x = dp(0)
        self.tank_y = dp(0)
        self.tank_velocity = dp(10)
        self.tank_size = dp(50)

        #bullet
        self.bullet = None
        self.bullet_size = dp(20)
        self.bullet_velocity = dp(5)
        self.bullet_removed = False
        self.bullet_on_screen = 0
        self.bullet_clock = None
        self.bullet_x = None
        self.bullet_y = None

        #enemy
        self.enemy = None
        self.enemy_count = 0
        self.enemy_size = dp(50)
        self.enemy_clock = None
        self.enemy_velocity = dp(2)

        
        
        super().__init__(**kwargs)

        with self.canvas:
            self.tank = Rectangle(pos = (self.tank_x, self.tank_y), size = (self.tank_size, self.tank_size))
            self.point = Label(pos = (self.width/2, self.height - 100), text = "Points: "+ str(self.points))

        Window.bind(on_key_down = self.keydown)
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        #adjust points label
        self.point.pos = ((self.width/2)-self.point_size/2, (self.height - 100)-self.point_size/2)


    def keydown(self, window, keycode, scancode, codepoint, modifiers):
        if codepoint == "a":
            self.update(move="a")
        if codepoint == "d":
            self.update(move="d")
        if codepoint == "w":
            self.update(move="w")
        if codepoint == "s":
            self.update(move="s")
        if codepoint == "i":
            self.update(move="i")

    def update(self, dt = None, move = None):
        x, y = self.tank.pos

        #tank movement
        if move == "a":
            if x > 0:
                x -= self.tank_velocity
        if move == "d":
            if x + self.tank_size < self.width:
                x += self.tank_velocity
        if move == "w":
            if y + self.tank_size < self.height:
                y += self.tank_velocity
        if move == "s":
            if y > 0:
                y -= self.tank_velocity
        self.tank.pos = (x,y)
        self.tank_x , self.tank_y = (x,y)

        #tank fire

        if move == "i" and self.bullet_on_screen == 0:
            with self.canvas:
                self.bullet_removed = False
                self.bullet_on_screen += 1
                self.bullet = Ellipse(pos = self.tank.pos, size = (self.bullet_size, self.bullet_size))
                if self.bullet_clock is None:
                    self.bullet_clock = Clock.schedule_interval(self.bullet_move, 1/60)
                
        #enemy generation
        if self.enemy_count < 1:
            with self.canvas:
                self.enemy = Rectangle(pos = (random.randint(0, self.width-50), self.height), size= (self.enemy_size, self.enemy_size))
                if self.enemy_clock is None:
                    self.enemy_clock = Clock.schedule_interval(self.enemy_move, 1/60)
            self.enemy_count +=1 

    #bullet move logic                  
    def bullet_move(self, dt):
        self.bullet_x, self.bullet_y = self.bullet.pos
        self.bullet_y += self.bullet_velocity
        self.bullet.pos = (self.bullet_x, self.bullet_y)
        
        if self.bullet_y > self.height and self.bullet_removed == False:
            self.canvas.remove(self.bullet)
            self.bullet = None
            self.bullet_removed = True
            self.bullet_on_screen -= 1
            if self.bullet_clock:
                self.bullet_clock.cancel()
                self.bullet_clock = None

    #enemy move logic
    def enemy_move(self, dt):
        enemy_x, enemy_y = self.enemy.pos
        enemy_y -= self.enemy_velocity
        self.enemy.pos = (enemy_x, enemy_y)
        
        #collision with enemy
        if enemy_y < 0 or (enemy_x < self.tank_x + self.tank_size and 
        enemy_x + self.enemy_size > self.tank_x and 
        enemy_y < self.tank_y + self.tank_size and 
        enemy_y + self.enemy_size > self.tank_y):
            self.canvas.remove(self.enemy)
            self.enemy_count -= 1
            if self.enemy_clock:
                self.enemy_clock.cancel()
                self.enemy_clock = None
            self.points = 0
            self.point.text = "Points: " + str(self.points)

        #hit enemy with bullet
        if self.bullet_x and self.bullet_y is not None:
            if (enemy_x < self.bullet_x + self.bullet_size and 
            enemy_x + self.enemy_size > self.bullet_x and 
            enemy_y < self.bullet_y + self.bullet_size and 
            enemy_y + self.enemy_size > self.bullet_y):
                self.canvas.remove(self.enemy)
                self.enemy_count -= 1
                if self.enemy_clock:
                    self.enemy_clock.cancel()
                    self.enemy_clock = None
                self.points += 1
                
                self.point.text = "Points: "+ str(self.points)

                  
class WindowManager(ScreenManager):
    pass
class GameScreen(Screen):
    pass
class MenuScreen(Screen):
    pass

class MenuWidget(Widget):
    pass        
            
class GameApp(App):
    pass


GameApp().run()