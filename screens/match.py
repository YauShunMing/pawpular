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
    in_layout:in_layout
    name:'match'
    MDBoxLayout:    
        md_bg_color: [0, 1, 1, 1]
        size_hint_y: None
        height: root.height
        width:root.width
        SnapScroll:
            layout:layout
            in_layout:in_layout
            MDBoxLayout:
                id:layout
                orientation:'vertical'
                adaptive_height:True
                MDBoxLayout:
                    md_bg_color: [0,0,0,0]
                    size_hint_y: None
                    width:root.width
                    height:root.height                 
                    SnapScrollH:
                        in_layout:in_layout
                        MDBoxLayout:                
                            id:in_layout
                            orientation: 'horizontal'
                            adaptive_width: True
                            MatchCard:
                                width: root.width
                                height:root.height
                                source:'assets/img/dog_1.jpg'
                            MatchCard:
                                width: root.width                    
                                height:root.height
                            MatchCard:
                                width: root.width                    
                                height:root.height 
                MDBoxLayout:
                    md_bg_color: [0,0,0,0]
                    size_hint_y: None
                    width:root.width
                    height:root.height                 
                    SnapScrollH:
                        in_layout:in_layout
                        MDBoxLayout:                
                            id:in_layout
                            orientation: 'horizontal'
                            adaptive_width: True
                            MatchCard:
                                width: root.width
                                height:root.height
                                source:'assets/img/dog_2.jpg'
                            MatchCard:
                                width: root.width                    
                                height:root.height
                            MatchCard:
                                width: root.width                    
                                height:root.height  
                MDBoxLayout:
                    md_bg_color: [0,0,0,0]
                    size_hint_y: None
                    width:root.width
                    height:root.height                 
                    SnapScrollH:
                        in_layout:in_layout
                        MDBoxLayout:                
                            id:in_layout
                            orientation: 'horizontal'
                            adaptive_width: True
                            MatchCard:
                                width: root.width
                                height:root.height
                                source:'assets/img/dog_3.jpg'
                            MatchCard:
                                width: root.width                    
                                height:root.height
                            MatchCard:
                                width: root.width                    
                                height:root.height                                                                               
    MDBoxLayout:        
        orientation: 'horizontal'
        size_hint_y: None
        height: 0.01*root.width
        pos_hint:{'bottom':0}
        MDProgressBar:
            value:50
"""
)

class Match(Screen):
    pass
