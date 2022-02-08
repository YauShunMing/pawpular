from kivy.app import App
from kivy.uix.video import Video
import os

os.environ['KIVY_VIDEO'] = 'ffpyplayer'

class APPPP(App):
    def build(self):
        video = Video(source='assets/video/video_3.mp4',)
        return video


if __name__ == '__main__':
    APPPP().run()