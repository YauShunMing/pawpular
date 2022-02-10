from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang.builder import Builder
from kivy.properties import DictProperty
from uix.snapscroll import SnapScroll

Builder.load_string(
"""
<MatchCard>:
    md_bg_color: [0, 0, 1, 1]
    size_hint_y: None
    size_hint_x: None
    Image:
        source: 'assets/img/dog_1.jpg'
        pos_hint: {'center_x':.5, 'top':1}
"""
)

class MatchCard(MDBoxLayout):
    pass


# MDProgressBar:
#     orientation: "vertical"
#     pos_hint:{"top":1,"right":1.5}
#     size_hint_x:None
#     width:'5dp'
#     color: (1,0,1,1)
#     min:0
#     max:4
#     value:1
#     reversed:True