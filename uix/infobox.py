from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from uix.infocard import InfoCard


Builder.load_string(
"""
<InfoBox>:
    id:info_box
    orientation:'vertical'
    size_hint: (1,0.3)
    spacing: '20dp'
    InfoCard:
        drag_rect_height: 
        drag_timeout: 10000000
        drag_distance: 0    

"""
)

class InfoBox(MDFloatLayout):
    pass