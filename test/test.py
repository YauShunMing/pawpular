# scrollview vertical and horizontal
# lcpallares
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang.builder import Builder

 
 
Builder.load_string(
"""
<MainWid>:
    BoxLayout:
        ScrollView:
            GridLayout:
                id: container_y
                size_hint_y: None
                cols: 1
                row_default_height: root.height*0.2
                height: self.minimum_height
    BoxLayout:
        ScrollView:
            GridLayout:
                id: container_x
                size_hint_x: None
                rows: 1
                col_default_width: root.width*0.2
                width: self.minimum_width
"""
)


class MainWid(BoxLayout):
    def __init__(self):
        super(MainWid, self).__init__()
        for i in range(30):
            self.ids.container_y.add_widget(Button(text=f"Botony: {i}"))
        for i in range(30):
            self.ids.container_x.add_widget(Button(text=f"Botonx: {i}"))
 
 
class MainApp(App):
    title = "Scroll view"
 
    def build(self):
        return MainWid()
 
 
if __name__ == "__main__":
    MainApp().run()
 
