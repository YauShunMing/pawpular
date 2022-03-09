from kivy.lang.builder import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.properties import DictProperty,StringProperty
from uix.snapscroll import SnapScroll
from kivy.uix.accordion import Accordion
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard

Builder.load_string(
"""
<InfoCard>:
    md_bg_color: (1,1,1,1)
    border_radius:20
    radius: [15]
    pos_hint:{'y':-.9}
    MDIconButton:
        id: md_icon_button
        icon:'arrow-up-bold'
        pos_hint:{'top':1}
        size_hint:(0.1,0.1)
        theme_icon_color: "Custom"
        icon_color: (0,0,0,.5)
        md_bg_color:(1,1,0,0.2)
        on_release: self.parent.expand()
"""
)

class InfoCard(MDCard):
    def expand(self):
        #making the info card moving upward to show the full picture
        if self.pos_hint != {'y':0}:
            self.pos_hint = {'y':0}
            self.ids.md_icon_button.pos_hint = {'bottom':1}
        #if you click again, its moving back to the original position
        else:
            self.pos_hint = {'y':-0.9}
            self.ids.md_icon_button.pos_hint = {'top':1}
