from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from data import data as users
from uix.videocard import VideoCard
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.app import App


Builder.load_string(
"""
<Feed>:
    layout:layout
    name:'feed'
    MDBoxLayout:    
        md_bg_color: [0, 0, 0, 1]
        size_hint_y: None
        height: root.height
        SnapScroll:
            layout: layout
            MDBoxLayout:
                id: layout
                orientation: 'vertical'
                adaptive_height: True       
"""
)

class Feed(Screen):
    data = []
    def __init__(self, **kw):
        for profile in users:
            _data = {
                'name':profile['name'],
                'source':profile['video'],
                'caption':profile['caption'],
                'song_name':profile['song_name'],
                'profile_pic':profile['profile_pic'],
                'likes':profile['likes'],
                'comments':profile['comments'],
                'shares':profile['shares'],
                'album_pic':profile['album_pic'],
            }
            self.data.append(_data)
        super().__init__(**kw)
        
    def on_enter(self, *args):
        print(self.data)
        for data in self.data:
            video_card = VideoCard()
            video_card.data = data
            video_card.height = Window.size[1] - dp(50)
            if self.data.index(data) == 0:
                # if the video is the first, play it
                video_card.video_state = 'play'

            self.layout.add_widget(video_card)
        return super().on_enter(*args)