from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_string(
"""
<NavBar>:
    md_bg_color: [0, 0, 0, 1]
    orientation: 'vertical'
    height: dp(50)
    size_hint_y: None
    MDBoxLayout:
        padding: '10dp', '5dp'
        spacing: '5dp'
        NavIcon:
            text: 'Match'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'match'        
        NavIcon:
            text: 'Feed'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'feed'
        NavIcon:
            text: 'Event'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'event'
        NavIcon:
            text: 'Setting'
            icon_size: '18sp'
            text_size: '10sp'
            screen: 'setting'
    MDBoxLayout:
        size_hint_y: None
        height: '5dp'
"""
)

class NavBar(MDBoxLayout):
    pass