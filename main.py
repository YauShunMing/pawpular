import os 
import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition,ScreenManager
from kivymd.font_definitions import theme_font_styles
from screens.screens import *
from uix.uix import * 
from kivy.core.text import LabelBase

os.environ['KIVY_VIDEO'] = 'ffpyplayer'

Window.size = (310,600)


class WindowManager(ScreenManager):
    pass

class Tiktok(MDApp):
    def build(self):
        self.wm = WindowManager(transition=FadeTransition())
        self.theme_cls.theme_style = 'Dark'

        #registering the Tiktok font so we can use the icons
        LabelBase.register(name='TikTokIcons',fn_regular='TiktokIcons.ttf')
        theme_font_styles.append('TiktokIcons')
        self.theme_cls.font_styles['TiktokIcons'] = ['TiktokIcons',16,False,0.15]

        screens = [
            Home(name='home')

        ]

        for screen in screens:
            self.wm.add_widget(screen)



        return self.wm

if __name__ =='__main__':
    Tiktok().run()
