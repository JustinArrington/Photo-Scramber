from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from PhotoShuffle import PhotoShuffle
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage


class ScatterTextWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ScatterTextWidget, self).__init__(**kwargs)
        self.image = PhotoShuffle('image.png')
        self.shuffleEvent = None
        self.sortEvent = None

    def firstClicked(self):
        self.reloadImage()

    def shuffleImage(self):
        self.image.shuffle()
        self.reloadImage()

    def startShuffle(self):
        self.shuffleEvent = Clock.schedule_interval(self.shuffleOnce, .01)

    def shuffleOnce(self, *args):
        for x in range(30000):
            self.image.shuffleOnce()
        self.reloadImage()

    def stopShuffling(self):
        Clock.unschedule(self.shuffleEvent)
        self.reloadImage()

    def sortImage(self):
        self.image.sortPixels()
        self.reloadImage()

    def startSort(self):
        Clock.unschedule(self.shuffleEvent)
        self.sortEvent = Clock.schedule_interval(self.sortOnce, .01)

    def sortOnce(self, *args):
        for x in range(10000):
            if self.image.sortOnce() is not None:
                Clock.unschedule(self.sortEvent)
                break
        self.reloadImage()
    def stopAll(self):
        Clock.unschedule(self.shuffleEvent)
        Clock.unschedule(self.sortEvent)
    def reloadImage(self):
        byteImage = self.image.ImgAsByteArray()
        im = CoreImage(byteImage, ext='png')
        label = self.ids['image']
        label.texture = im.texture


class ImageApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    Window.size = (1280, 1080)
    ImageApp().run()
