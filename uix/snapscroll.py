from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty

Builder.load_string(
"""
<SnapScroll>:
    scroll_distance: 500 # help prevent kivy detecting scroll in on drag
    bar_width: 0
    scroll_wheel_distance:0 #disable mouse scrolling

""")

class SnapScroll(ScrollView):
    layout = ObjectProperty() # adapative layout inside the scrollview, where widgets are added to 

    def on_scroll_start(self,touch,check_children = True):
        touch.ud['pos'] = self.to_local(*touch.pos) #saving the touched location saved by the user
        for widget in self.layout.children: #looping through all widget to get the clicked widget 
            if widget != self:
                if widget.collide_point(*touch.ud['pos']):
                    touch.ud['widget'] = widget #saving the widget that received the touch
                    touch.ud['index'] = self.layout.children.index(widget) #and its index        

        return super().on_scroll_start(touch,check_children=check_children)

    def on_scroll_stop(self,touch,check_children=True):
        self._touch = None # cancel the touch
        local_touch = self.to_local(*touch.pos)

        print(self.layout.children, touch.ud['index'])

        if local_touch[1] > touch.ud['pos'][1]: # compare current touch pos with the one we saved , to know the direction the user is scrolling
        
            if touch.ud['index'] != 0: #if widget is not the first, scroll up 
                self.scroll_to(self.layout.children[touch.ud['index'] -1], padding=0)
                self.layout.children[touch.ud['index']-1].video_state = 'play' # play next video
                self.layout.children[touch.ud['index']].video_state = 'pause' # pause current video
        elif local_touch[1] < touch.ud['pos'][1]:
            if touch.ud['index'] < len(self.layout.children) - 1: # if widget is not the last, scroll down
                self.scroll_to(self.layout.children[touch.ud['index'] +1], padding=0)
                self.layout.children[touch.ud['index']+1].video_state = 'play' # play prev video
                self.layout.children[touch.ud['index']].video_state = 'pause' # pause current video

        print('on scroll stop >>>', local_touch)
        
        touch.ud.pop('pos')
        return True
