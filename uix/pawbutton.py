from kivy.lang.builder import Builder
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

Builder.load_string(
"""
<PawButton>:
    source: 'assets/img/paw_button.png' 
    pos_hint:{'y':-0.08,'center_x':0.5}
    size_hint:0.3,0.3

"""
)

class PawButton(ButtonBehavior,Image):
    pass