from kivy.lang.builder import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty

Builder.load_string(
"""
<SnapScroll>:
    scroll_distance: 500 # helps prevent kivy detecting multiple scroll in one drag.
    bar_width: 0
    scroll_wheel_distance: 0 # disable mouse scrolling
"""
)

class SnapScroll(ScrollView):
    layout = ObjectProperty() # The adaptive layout inside the scrollview; where widgets are added to
    in_layout  = ObjectProperty()

    def on_scroll_start(self, touch, check_children=True):
        touch.ud['out_pos'] = self.to_local(*touch.pos) # saving the touch pos clicked by the user.
        for widget in self.layout.children: # Looping through all widget to get the clicked widget
            if widget != self:
                if widget.collide_point(*touch.ud['out_pos']):
                    touch.ud['out_widget'] = widget # saving the widget that recieved the touch
                    touch.ud['out_index'] = self.layout.children.index(widget) # and its index
                    #print(touch.ud, self.layout.children)

        return super().on_scroll_start(touch, check_children=check_children) # Make sure you return this

    def on_scroll_stop(self, touch, check_children=True):
        self._touch = None # cancel touch
        local_touch = self.to_local(*touch.pos)

        # print('out scroll stop detected')

        # print('out touch ud', touch.ud['in_pos'], touch.ud['out_pos'])
        # print('out local_touch', local_touch)        

        # if abs(local_touch[1] - touch.ud['out_pos'][1]) < 50:

        #     if local_touch[0] < touch.ud['in_pos'][0]: # Comparing current touch pos with the one we saved.
        #                                             # to know the direction the user is scrolling. 
        #         if touch.ud['in_index'] != 0: # If widget is not the first, scroll up
        #             self.scroll_to(self.in_layout.children[touch.ud['in_index']-1], padding=0)
        #             #print(abs(local_touch[1] - local_touch[1]))
        #             self.in_layout.children[touch.ud['in_index']-1].video_state = 'play' # play next video
        #             self.in_layout.children[touch.ud['in_index']].video_state = 'pause' # pause current video

        #             print('right....', local_touch[0],touch.ud['in_pos'][0])

        #     elif local_touch[0] > touch.ud['in_pos'][0]:
        #         if touch.ud['in_index'] < len(self.in_layout.children)-1: # If widget is not the last, scroll down
        #             self.scroll_to(self.in_layout.children[touch.ud['in_index']+1], padding=0)
        #             #print(abs(local_touch[1] - local_touch[1]))
        #             self.in_layout.children[touch.ud['in_index']+1].video_state = 'play' # play prev video
        #             self.in_layout.children[touch.ud['in_index']].video_state = 'pause' # pause current video

        #             print('left...', local_touch[0],touch.ud['pos'][0])

            

        if abs(local_touch[0] - touch.ud['out_pos'][0]) < 50:

            if local_touch[1] > touch.ud['out_pos'][1]: # Comparing current touch pos with the one we saved.
                                                    # to know the direction the user is scrolling. 
                if touch.ud['out_index'] != 0: # If widget is not the first, scroll up
                    self.scroll_to(self.layout.children[touch.ud['out_index']-1], padding=0)
                    self.layout.children[touch.ud['out_index']-1].video_state = 'play' # play next video
                    self.layout.children[touch.ud['out_index']].video_state = 'pause' # pause current video

                    #print('up....', local_touch[0],touch.ud['out_pos'][0])

            elif local_touch[1] < touch.ud['out_pos'][1]:
                if touch.ud['out_index'] < len(self.layout.children)-1: # If widget is not the last, scroll down
                    self.scroll_to(self.layout.children[touch.ud['out_index']+1], padding=0)

                    self.layout.children[touch.ud['out_index']+1].video_state = 'play' # play prev video
                    self.layout.children[touch.ud['out_index']].video_state = 'pause' # pause current video

                    #print('down...', local_touch[0],touch.ud['out_pos'][0])

        if 'out_pos' in touch.ud.keys():
            touch.ud.pop('out_pos') # we are done with the pos we save so we clear it
        # if 'in_pos' in touch.ud.keys():
        #     touch.ud.pop('in_pos')
        return True #...........
