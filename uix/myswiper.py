from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from uix.videocard import VideoCard
from uix.matchcard import MatchCard
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.app import App
from kivymd.uix.swiper import MDSwiperItem
from kivy.properties import StringProperty

# Builder.load_string(
# """
# <MySwiper@MDSwiperItem>
#     FitImage:
#         source: root.source
#         radius: [20,]
# """
# )

# class MySwiper(MDSwiperItem):
#     source  = StringProperty(None)


