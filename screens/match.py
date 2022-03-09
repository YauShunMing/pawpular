from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from uix.videocard import VideoCard
from uix.matchcard import MatchCard
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.app import App


Builder.load_string(
"""
<Match>:
    #layout:layout
    name:'match'
    MDFloatLayout:
        md_bg_color:(0,0,1,0.2)
        MDBoxLayout:    
            size_hint_y: None
            height: root.height
            width:root.width
            SnapScroll:
                layout:layout
                MDBoxLayout:
                    id:layout
                    orientation:'vertical'
                    adaptive_height:True
                    MDBoxLayout:
                        md_bg_color: [0,0,0,0]
                        size_hint_y: None
                        width:root.width
                        height:root.height                 
                        MDSwiper:                        
                            items_spacing: '5dp'
                            size_durration: 0.1
                            size_hint_y: None
                            height: root.height
                            size_hint_x: None
                            width: root.width
                            MySwiper:
                                img: 'assets/img/dog_1.jpg'
                            MySwiper:
                                img: 'assets/img/dog_2.jpg'
                            MySwiper:
                                img: 'assets/img/dog_3.jpg'
                    MDBoxLayout:
                        md_bg_color: [0,0,0,0]
                        size_hint_y: None
                        width:root.width
                        height:root.height                 
                        MDSwiper:                        
                            items_spacing: '5dp'
                            size_durration: 0.1
                            size_hint_y: None
                            height: root.height
                            size_hint_x: None
                            width: root.width
                            MySwiper:
                                img: 'assets/img/image_1.jpg'
                            MySwiper:
                                img: 'assets/img/image_2.jpg'
                            MySwiper:
                                img: 'assets/img/image_3.jpg'                            
        PawButton
        InfoBox
"""
)

class Match(Screen):
    pass
